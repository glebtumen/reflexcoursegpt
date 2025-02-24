import reflex as rx

data: list[dict[str, str]] = [
    {
        "question": "Сколько работ я могу сделать, если оформлю доступ на неделю?",
        "answers": "После получения доступа можно делать неограниченное количество работ в течение недели",
    },
    {
        "question": "Как сделать работу по своему содержанию?",
        "answers": "Нужно использовать режим Курсовая по содержанию, ввести тему и содержание работы.",
    },
    {
        "question": "Подходит для дипломов или курсовых?",
        "answers": "Да, можно настроить как для дипломов, так и для курсовых.",
    },
    {
        "question": "Мои сгенерированные тексты будут храниться или использоваться?",
        "answers": "Нет, текст хранится только в твоём браузере. Как только вкладка обновится или закроется, текст удалится навсегда.",
    },
    {
        "question": "Как делать несколько работ одновременно?",
        "answers": "Нужно открыть несколько вкладок с главной страницей и ввести тему. Так запустится процесс генерации сразу нескольких работ.",
    },
]


def txt(string: str, shade: int, weight: str = "bold") -> rx.Component:
    return rx.text(
        string,
        color=rx.color("gray", shade),
        size="4",
        class_name=f"tracking-[-0.035em] font-manrope font-bold font-{weight}",
    )


def question_and_answer(question: str, answer: str):
    return rx.hstack(
        rx.vstack(
            txt(question, 12, "bold"),
            txt(answer, 11, "light"),
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
