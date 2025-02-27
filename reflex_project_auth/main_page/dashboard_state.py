import os
from openai import AsyncOpenAI
import reflex as rx
from typing import Union, Any, List, Dict
from dotenv import load_dotenv
import json

load_dotenv()


class WorkflowState(rx.State):
    search: bool = False
    prepare: bool = False
    docx: bool = False

    language: str = "ru"
    points: str = "5"
    detail: str = "Краткий обзор"
    detail_description: str = ""
    creativity: int = 6
    mode: str = "course"

    work_title: str = ""
    chat_history: list[tuple[str, str]] = []

    is_processing: bool = False
    _task_running: bool = False

    def on_load(self):
        """Initialize state when a new client connects."""
        self.search = False
        self.prepare = False
        self.docx = False
        self.points = "5"
        self.creativity = 6
        self.language = "Русский"
        self.detail = "Краткий обзор"
        self.detail_description = ""
        self.work_title = ""
        self.chat_history = []
        self.is_processing = False
        self._task_running = False

    @rx.event
    def set_creativity(self, value: List[Union[int, float]]) -> None:
        self.creativity = int(value[0])

    @rx.event
    def on_language_change(self, value: str):
        self.language = value

    @rx.event
    def set_mode(self, value: str):
        self.mode = value
        return WorkflowState.on_load

    @rx.event
    def on_points_change(self, value: str):
        self.points = value

    @rx.event
    def on_detail_change(self, value: str):
        if value == "Краткий обзор":
            self.detail_description = """
            лаконичный и сжатый текст, который кратко изложит основные идеи и ключевые моменты темы. 
            Убедитесь, что информация представлена ясно и понятно, чтобы читатели могли быстро 
            ознакомиться с материалом или использовать его как введение к более глубокому изучению. 
            Объем текста должен быть ограничен, сосредоточив внимание на самых важных аспектах без лишних деталей
            Размер текста около 250 слов
            """
            self.detail = value

        elif value == "Средний обзор":
            self.detail_description = """
            Включите основные идеи, дополненные примерами и объяснениями, 
            чтобы читатели могли получить более полное представление о теме. Этот вариант должен 
            предоставить баланс между краткостью и полнотой изложения, не углубляясь в чрезмерную 
            детализацию. Объем текста должен быть умеренным.
            Стилевые приёмы:
            Чередуй длинные (25+ слов) и короткие (до 8 слов) предложения
            Используй инверсию в 1-2 предложениях на абзац
            Добавь 2-3 уточняющих комментария в скобках
            Используй простые и сложносочиненные предложения для улучшения читаемости.
            Запрещены риторические вопросы и разговорные конструкции  
            70% терминов из глоссария: названия теорий, термины
            Размер текста около 400 слов
            """
            self.detail = value

        elif value == "Подробный обзор":
            self.detail_description = """
            развернутый текст, который обеспечит наиболее полное и глубокое освещение темы. 
            Включите все ключевые аспекты, примеры, детали и дополнительные пояснения. 
            Этот обзор должен быть полезен для читателей, которые хотят полностью разобраться в 
            предметной области или подготовить основательное исследование. Объем текста должен быть 
            значительным, охватывая все важные нюансы и аспекты рассматриваемого вопроса.
            Сложные термины объясни без потери их смысла.
            используй различные структуры предложений и лексическое разнообразие для более естественного стиля изложения
            Стилевые приёмы:
            Чередуй длинные (25+ слов) и короткие (до 8 слов) предложения
            Используй инверсию в 1-2 предложениях на абзац
            Добавь 2-3 уточняющих комментария в скобках
            Добавь детали для контекста,Обогати текст глубоким анализом оставляя профессиональный научный жаргон.
            Используй простые и сложносочиненные предложения для улучшения читаемости.
            Запрещены риторические вопросы и разговорные конструкции  
            70% терминов из глоссария: названия теорий, термины
            Размер текста 500 слов и более"""
            self.detail = value

    def get_session_data(self) -> dict:
        """Return session-specific data."""
        return {
            "work_title": self.work_title,
            "chat_history": self.chat_history,
        }

    async def generate_content(self, prompt: str) -> str:
        """Generate a single variant using OpenAI API."""
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        temperature = self.creativity / 10
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Ты - профессионал со знаниями в науке, который помогает студентам писать курсовые работы. Ты должен писать ответы максимально полно и так, будто они были написаны студентом.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )

        return response.choices[0].message.content

    async def generate_content_table(self, prompt: str) -> str:
        """Generate a single variant using OpenAI API."""
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        temperature = self.creativity / 10
        language = self.language
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"Пиши на {language} языке/ Ты - профессионал со знаниями в науке, который помогает студентам писать курсовые работы. Ты должен писать ответы максимально полно и так, будто они были написаны студентом.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content

    @rx.event
    def set_work_title(self, form: dict[str, Any]) -> None:
        """Set work title and trigger workflow."""
        self.work_title = form.get("title", "")
        self.is_processing = True
        if self.mode == "free":
            self.work_title = ""
            return WorkflowState.send_free_message
        else:
            return WorkflowState.execute_workflow

    @rx.event
    def stop_workflow(self) -> None:
        """Stop workflow."""
        self._task_running = False
        self.is_processing = False

    @rx.event
    def delete_work_title(self) -> None:
        """Reset all state for current session."""
        self.work_title = ""
        self.chat_history = []
        self.is_processing = False
        self._task_running = False

        # Clear local storage for this session
        rx.remove_local_storage("work_title")

    @rx.event(background=True)
    async def send_free_message(self) -> None:
        """Append a new free chat message and generate a response."""
        async with self:
            if self._task_running:
                return
            self._task_running = True

        async with self:
            self.chat_history.append(("Пользователь:", self.work_title))
            self.chat_history.append(("КурсачГПТ:", "Генерация..."))
        try:
            response_text = await self.generate_content(self.work_title)
            async with self:
                self.chat_history[-1] = ("КурсачГПТ:", response_text)

        except Exception as e:
            async with self:
                self.chat_history.append(("Ошибка", f"Произошла ошибка: {str(e)}"))
        finally:
            async with self:
                self._task_running = False
                self.is_processing = False

    @rx.event(background=True)
    async def execute_workflow(self) -> None:
        """Execute the main workflow as a background task with interactive section generation."""
        async with self:
            if self._task_running:
                return
            self._task_running = True
            self.chat_history = []

        try:
            # Generate Introduction with multiple variants
            table_for_intro = """
            Вступление курсовой работы
            Актуальность курсовой работы

            Объект курсовой работы
            Предмет курсовой работы

            Цель данной курсовой работы (связана с предметом курсовой работы)
            1)Задача 1;
            2)Задача 2;
            3)Задача 3;
            4)Задача 4;
            5)Задача 5;"""

            intro_prompt = f"""
                    Пожалуйста, напишите введение для моей курсовой работы на тему [{ self.work_title }].
                    Введение должно предоставить четкий и краткий обзор темы, включая ее актуальность и значимость.
                    Пожалуйста, убедитесь, что ваше написание подходит для научной аудитории.
                    Ваш ответ должен быть хорошо структурирован, с логическим потоком мыслей и четким тезисом.
                    Структура введения: вступление из 2-3 абзацев; актуальность;  объект и предмет изучения;
                    задачи; краткий обзор -
                    Строго следуй этой структуре: { table_for_intro }
                    Пиши на на языке: {self.language}.
                    Количество текста: {self.detail_description}."""

            async with self:
                if not self._task_running:
                    return
                self.chat_history.append(("Введение:", "Генерация..."))

            intro = await self.generate_content(intro_prompt)

            async with self:
                if not self._task_running:
                    return
                self.chat_history[-1] = ("Введение:", intro)

            # Generate Ending
            outro_prompt = f"""
                    Напишите заключение для моей курсовой работы на тему "{ self.work_title }",
                    в котором подчеркивается актуальность темы и указываются потенциальные
                    преимущества предмета темы. Ваше заключение должно  подчеркивать важность
                    темы для решения текущих мировых проблем. Пожалуйста, убедитесь, что ваш вывод четкий,
                    лаконичный и хорошо структурированный.
                    Пиши на на языке: {self.language}.
                    Количество текста: {self.detail_description}."""

            async with self:
                if not self._task_running:
                    return
                self.chat_history.append(("Заключение:", "Генерация..."))
            outro = await self.generate_content(outro_prompt)

            async with self:
                if not self._task_running:
                    return
                self.chat_history[-1] = ("Заключение:", outro)

            # Generate Content Structure with multiple variants
            table_for_content = f"""
                    {"{"}
                "theory":"Сюда вставить название ТЕОРЕТИЧЕСКОЙ ЧАСТИ(Придумай как назвать теоретическую часть работы)",
                "theory_points":
                    {"{"}
                        "point1": "сюда вставить пункты теоретической части. сделай {self.points} пунктов",
                    {"}"},
                "practice":"Сюда вставить название ПРАКТИЧЕСКОЙ ЧАСТИ(Придумай как назвать ПРАКТИЧЕСКуй ЧАСТь работы)",
                "practice_points":
                    {"{"}
                        "point1": "сюда вставить пункты ПРАКТИЧЕСКОЙ части. сделай {self.points} пунктов",
                    {"}"},
            {"}"}
            """

            content_prompt = f"""
                    Напиши содержание для моей курсовой работы на тему { self.work_title }. 
                    Используй формальный язык. Ваш ответ должен быть хорошо структурирован, 
                    с логическим потоком мыслей. строго следуй этой структуре:  { table_for_content }. 
                    Ответ отправь в виде JSON без форматирования, отправляй строго json без md форматирования, 
                    отправляй json 
                    Пиши на на языке: {self.language}."""

            async with self:
                if not self._task_running:
                    return
                self.chat_history.append(("Содержание:", "Генерация..."))
            content_table = await self.generate_content_table(content_prompt)

            async with self:
                if not self._task_running:
                    return

                try:
                    content_struct = json.loads(content_table)
                except Exception as e:
                    self.chat_history[-1] = (
                        "Содержание:",
                        f"Ошибка парсинга содержимого: {str(e)}",
                    )
                    return

                if content_struct:
                    readable = (
                        f"Теоретическая часть: {content_struct.get('theory', '')}\n"
                    )
                    for key, point in content_struct.get("theory_points", {}).items():
                        readable += f" - {point}\n\n"
                    readable += (
                        "\nПрактическая часть: "
                        + content_struct.get("practice", "")
                        + "\n"
                    )
                    for key, point in content_struct.get("practice_points", {}).items():
                        readable += f" - {point}\n\n"

                    self.chat_history[-1] = ("Содержание:", readable)

            # Process theory points
            for key, point in content_struct.get("theory_points", {}).items():
                async with self:
                    if not self._task_running:
                        return

                prompt_detail = f"""Создай текст на тему { point }, который может быть использован в качестве части курсовой работы на тему { self.work_title }.
            Убедись, что тональность и стиль написания соответствуют научной аудитории. 
            Количество текста: {self.detail_description}.
            Пиши на на языке: {self.language}.
            """

                async with self:
                    if not self._task_running:
                        return
                    self.chat_history.append((f"{point}", "Генерация..."))

                detail_text = await self.generate_content(prompt_detail)

                async with self:
                    if not self._task_running:
                        return
                    self.chat_history[-1] = (f"{point}", detail_text)

            # Process practice points
            for key, point in content_struct.get("practice_points", {}).items():
                async with self:
                    if not self._task_running:
                        return

                prompt_detail = f"""Создай текст на тему { point }, который может быть использован в качестве части курсовой работы на тему { self.work_title }.
            Убедись, что тональность и стиль написания соответствуют научной аудитории. 
            Количество текста: {self.detail_description}.
            Пиши на на языке: {self.language}.
            """

                async with self:
                    if not self._task_running:
                        return
                    self.chat_history.append((f"{point}", "Генерация..."))

                detail_text = await self.generate_content(prompt_detail)

                async with self:
                    self.chat_history[-1] = (f"{point}", detail_text)

            # Optional: Generate preparation questions if needed
            async with self:
                if self.prepare:
                    prepare_prompt = (
                        f"Составь список вопросов для защиты работы '{self.work_title}'"
                    )
                    self.chat_history.append(("Подготовка к защите:", "Генерация..."))

            if self.prepare:
                prepare_variants = await self.generate_content(prepare_prompt)

                async with self:
                    if not self._task_running:
                        return
                    self.chat_history[-1] = ("Подготовка к защите:", prepare_variants)

        except Exception as e:
            async with self:
                self.chat_history.append(("Ошибка", f"Произошла ошибка: {str(e)}"))
        finally:
            async with self:
                self._task_running = False
                self.is_processing = False
