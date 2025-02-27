import reflex as rx

data: list[dict[str, str]] = [
    {
        "question": "Сколько работ я могу сделать, если оформлю доступ на неделю?",
        "answers": "Можно делать неограниченное количество работ в течение срока доступа",
    },
    {
        "question": "Подходит для дипломов или курсовых?",
        "answers": "Да, можно использовать как для дипломов, так и для курсовых и других работ",
    },
    {
        "question": "Мои сгенерированные тексты будут храниться или использоваться?",
        "answers": "Нет, текст хранится только в твоём браузере. Как только вкладка обновится или закроется, текст удалится навсегда",
    },
    {
        "question": "Как делать несколько работ одновременно?",
        "answers": "Скопируй ссылку рабочей страницы и вставь в новых вкладках. Так можно делать сразу несколько работ одновременно",
    },
]


def txt(string: str, shade: int, weight: str = "bold") -> rx.Component:
    return rx.text(
        string,
        color=rx.color("gray", shade),
        size="4",
        class_name=f"text-black tracking-[-0.035em] text-[15px] font-manrope font-bold font-{weight}",
    )


def question_and_answer(question: str, answer: str):
    return rx.hstack(
        rx.vstack(
            txt(question, 12, "bold"),
            txt(answer, 11, "regular"),
            align="start",
            spacing="2",
        ),
        width="100%",
        align="start",
        padding="16px 0px",
        border_top=f"0.75px solid {rx.color('gray', 4)}",
    )


def faq_v1():
    return rx.vstack(
        *[question_and_answer(item["question"], item["answers"]) for item in data],
        width="100%",
        max_width="35em",
        height="100%",
    )
