import os
from openai import AsyncOpenAI
import reflex as rx
from typing import Union, Any, Optional, List
from dotenv import load_dotenv
import asyncio
import uuid

load_dotenv()


class WorkflowState(rx.State):
    search: bool = False
    prepare: bool = False
    docx: bool = False

    language: str = "ru"
    points: str = "5"
    detail: str = "Краткий обзор"
    creativity: int = 6
    mode: str = "course"

    work_title: str = ""
    chat_history: list[tuple[str, str]] = []

    is_processing: bool = False
    _task_running: bool = False
    show_sections: bool = True

    def on_load(self):
        """Initialize state when a new client connects."""
        self.search = False
        self.prepare = False
        self.docx = False
        self.points = "5"
        self.creativity = 6
        self.language = "Русский"
        self.detail = "Краткий обзор"
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
        self.detail = value

    def get_session_data(self) -> dict:
        """Return session-specific data."""
        return {
            "work_title": self.work_title,
            "chat_history": self.chat_history,
            "sections": self.sections,
        }

    async def generate_content(self, prompt: str, section_name: str) -> str:
        """Generate a single variant using OpenAI API."""
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        temperature = self.creativity / 10
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return response.choices[0].message.content

    @rx.event
    def set_work_title(self, form: dict[str, Any]) -> None:
        """Set work title and trigger workflow."""
        self.work_title = form.get("title", "")
        self.is_processing = True
        if self.mode == "free":
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
        self.sections = {}
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

        message = self.work_title
        async with self:
            self.chat_history.append(("Пользователь:", message))
            self.chat_history.append(("КурсачГПТ:", "Генерация..."))
        try:
            response_text = await self.generate_content(message)
            async with self:
                self.chat_history[-1] = ("КурсачГПТ:", response_text)
                self.work_title = ""
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
            intro_prompt = f"Напиши введение для работы с темой '{self.work_title}', Язык: {self.language}."
            async with self:
                self.chat_history.append(("Введение:", "Генерация..."))
            intro = await self.generate_content(intro_prompt, "Введение")
            if not self._task_running:
                return

            async with self:
                self.chat_history[-1] = ("Введение:", intro)
            # Generate Content Structure with multiple variants
            content_prompt = f"На основе введения, напиши содержание для работы '{self.work_title}' с {self.points} пунктами. Детализация: {self.detail}."
            async with self:
                self.chat_history.append(("Содержание:", "Генерация..."))
            content = await self.generate_content(content_prompt, "Содержание")
            if not self._task_running:
                return

            async with self:
                self.chat_history[-1] = ("Содержание:", content)

            # Optional: Generate preparation questions if needed
            if self.prepare:
                prepare_prompt = (
                    f"Составь список вопросов для защиты работы '{self.work_title}'"
                )
                async with self:
                    self.chat_history.append(("Подготовка к защите:", "Генерация..."))
                prepare_variants = await self.generate_content(
                    prepare_prompt, "Подготовка к защите"
                )
                if not self._task_running:
                    return
                async with self:
                    self.chat_history[-1] = ("Подготовка к защите:", prepare_variants)

        except Exception as e:
            async with self:
                self.chat_history.append(("Ошибка", f"Произошла ошибка: {str(e)}"))
        finally:
            async with self:
                self._task_running = False
