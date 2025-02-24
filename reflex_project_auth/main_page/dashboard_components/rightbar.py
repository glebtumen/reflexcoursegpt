import reflex as rx
from ..dashboard_state import WorkflowState


def right_sidebar() -> rx.Component:
    # Right Sidebar: Settings panel.
    return rx.box(
        rx.vstack(
            rx.heading(
                "Настройки",
                class_name="text-2xl tracking-[-0.055em] text-left font-bold font-manrope",
            ),
            rx.vstack(
                # Language selection.
                rx.box(
                    rx.tooltip(
                        rx.html(
                            "<u>Язык текста</u>",
                            class_name="text-sm font-medium",
                            margin_bottom="10px",
                        ),
                        content="Язык на котором будет написан документ",
                    ),
                    rx.select(
                        ["Русский", "English", "Kazakh"],
                        value=WorkflowState.language,
                        on_change=WorkflowState.on_language_change,
                        width="100%",
                    ),
                    width="100%",
                ),
                # Creativity slider.
                rx.box(
                    rx.hstack(
                        rx.tooltip(
                            rx.html(
                                f"<u>Креативность: {WorkflowState.creativity}</u>",
                                class_name="text-sm font-medium",
                                width="100%",
                            ),
                            content="Креативность определяет разнообразие терминов в тексте. Оптимальное значение: 0.6",
                        ),
                        justify="between",
                        margin_bottom="10px",
                    ),
                    rx.slider(
                        default_value=[6],
                        min_=2,
                        max=10,
                        step=1,
                        on_change=WorkflowState.set_creativity.throttle(100),
                        width="100%",
                        color=rx.color("gray", 12),
                    ),
                    width="100%",
                ),
                # Number of points in coursework.
                rx.box(
                    rx.tooltip(
                        rx.html(
                            "<u>Количество пунктов в курсовой</u>",
                            class_name="text-sm font-medium",
                            margin_bottom="10px",
                            width="100%",
                        ),
                        content="Сколько всего будет пунктов в курсовой работе",
                    ),
                    rx.select.root(
                        rx.select.trigger(
                            width="100%",
                        ),
                        rx.select.content(
                            rx.select.item("5", value="5"),
                            rx.select.item("10", value="10"),
                            rx.select.item("15", value="15"),
                            rx.select.item("20", value="20"),
                        ),
                        default_value="5",
                        on_change=WorkflowState.on_points_change,
                    ),
                    width="100%",
                ),
                # Detail level selection.
                rx.box(
                    rx.tooltip(
                        rx.html(
                            "<u>Детализация</u>",
                            margin_bottom="10px",
                            class_name="text-sm font-medium",
                        ),
                        content="Детализация определяет количество текста в пункте",
                    ),
                    rx.select(
                        ["Краткий обзор", "Средний обзор", "Подробный обзор"],
                        value=WorkflowState.detail,
                        on_change=WorkflowState.on_detail_change,
                        width="100%",
                    ),
                    width="100%",
                ),
                spacing="6",
            ),
            spacing="4",
        ),
        class_name="min-w-60 w-60 border-l p-4",
        height="100%",
    )
