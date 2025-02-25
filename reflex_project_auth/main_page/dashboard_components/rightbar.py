import reflex as rx
from ..dashboard_state import WorkflowState


def right_sidebar() -> rx.Component:
    # Right Sidebar: Settings panel.
    return rx.box(
        rx.vstack(
            rx.heading(
                "Настройки",
                class_name="text-xl font-semibold font-manrope",
            ),
            rx.vstack(
                # Language selection.
                rx.box(
                    rx.tooltip(
                        rx.vstack(
                            rx.html(
                                "Язык текста",
                                class_name="font-bold font-manrope text-[13px]",
                                margin_bottom="10px",
                            ),
                            rx.cond(
                                WorkflowState.is_processing,
                                rx.select(
                                    ["Русский", "English", "Kazakh"],
                                    value=WorkflowState.language,
                                    on_change=WorkflowState.on_language_change,
                                    width="100%",
                                    disabled=True,
                                ),
                                rx.select(
                                    ["Русский", "English", "Kazakh"],
                                    value=WorkflowState.language,
                                    on_change=WorkflowState.on_language_change,
                                    width="100%",
                                    disabled=False,
                                ),
                            ),
                            spacing="0",
                        ),
                        content="Язык на котором будет написан документ",
                    ),
                    width="100%",
                ),
                # Creativity slider.
                rx.box(
                    rx.tooltip(
                        rx.vstack(
                            rx.html(
                                f"Креативность: {WorkflowState.creativity}",
                                class_name="font-bold font-manrope text-[13px]",
                                width="100%",
                            ),
                            rx.slider(
                                default_value=[6],
                                high_contrast=True,
                                min_=2,
                                max=10,
                                step=1,
                                on_change=WorkflowState.set_creativity.throttle(100),
                                width="100%",
                                color_scheme="gray",
                                size="1",
                            ),
                            spacing="2",
                        ),
                        content="""Определяет разнообразие текста.\n
                        Рекомендуемое значение для гуманитарных работ: 6\n
                        Рекомендуемое значение для технических работ: 4""",
                    ),
                    width="100%",
                ),
                # Number of points in coursework.
                rx.box(
                    rx.tooltip(
                        rx.vstack(
                            rx.html(
                                "Количество пунктов в главе",
                                class_name="font-bold font-manrope text-[13px]",
                                margin_bottom="10px",
                                width="100%",
                            ),
                            rx.cond(
                                WorkflowState.is_processing,
                                rx.select.root(
                                    rx.select.trigger(
                                        width="100%",
                                    ),
                                    rx.select.content(
                                        rx.select.item("3", value="3"),
                                        rx.select.item("5", value="5"),
                                        rx.select.item("7", value="7"),
                                        rx.select.item("9", value="9"),
                                    ),
                                    default_value="5",
                                    on_change=WorkflowState.on_points_change,
                                    disabled=True,
                                ),
                                rx.select.root(
                                    rx.select.trigger(
                                        width="100%",
                                    ),
                                    rx.select.content(
                                        rx.select.item("3", value="3"),
                                        rx.select.item("5", value="5"),
                                        rx.select.item("7", value="7"),
                                        rx.select.item("9", value="9"),
                                    ),
                                    default_value="5",
                                    on_change=WorkflowState.on_points_change,
                                    disabled=False,
                                ),
                            ),
                            spacing="0",
                        ),
                        content="Определяет количество пунктов в теории и практике",
                    ),
                    width="100%",
                ),
                # Detail level selection.
                rx.box(
                    rx.tooltip(
                        rx.vstack(
                            rx.html(
                                "Детализация",
                                margin_bottom="10px",
                                class_name="font-bold font-manrope text-[13px]",
                            ),
                            rx.select(
                                ["Краткий обзор", "Средний обзор", "Подробный обзор"],
                                value=WorkflowState.detail,
                                on_change=WorkflowState.on_detail_change,
                                width="100%",
                            ),
                            spacing="0",
                        ),
                        content="Определяет подробность текста в каждом пункте",
                    ),
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.cond(
                            WorkflowState.is_processing,
                            rx.checkbox(
                                on_change=WorkflowState.set_search,
                                color_scheme="gray",
                                disabled=True,
                            ),
                            rx.checkbox(
                                on_change=WorkflowState.set_search,
                                color_scheme="gray",
                                disabled=False,
                            ),
                        ),
                        rx.text(
                            "Использовать поиск в интернете",
                            class_name="font-bold font-manrope text-[13px]",
                        ),
                    ),
                    rx.hstack(
                        rx.cond(
                            WorkflowState.is_processing,
                            rx.checkbox(
                                on_change=WorkflowState.set_prepare,
                                color_scheme="gray",
                                disabled=True,
                            ),
                            rx.checkbox(
                                on_change=WorkflowState.set_prepare,
                                color_scheme="gray",
                                disabled=False,
                            ),
                        ),
                        rx.text(
                            'Добавить секцию "Подготовка к защите"',
                            class_name="font-bold font-manrope text-[13px]",
                        ),
                    ),
                    rx.hstack(
                        rx.cond(
                            WorkflowState.is_processing,
                            rx.checkbox(
                                on_change=WorkflowState.set_docx,
                                color_scheme="gray",
                                disabled=True,
                            ),
                            rx.checkbox(
                                on_change=WorkflowState.set_docx,
                                color_scheme="gray",
                                disabled=False,
                            ),
                        ),
                        rx.text(
                            "Вывести текст в файл word.docx",
                            class_name="font-bold font-manrope text-[13px]",
                        ),
                    ),
                    spacing="4",
                    margin_top="1em",
                    height="100%",
                ),
                spacing="6",
            ),
            spacing="4",
        ),
        class_name="min-w-60 w-60 border-l p-4",
        height="100%",
    )
