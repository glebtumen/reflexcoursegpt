import reflex as rx
from ..dashboard_state import WorkflowState


def main_content() -> rx.Component:
    return rx.vstack(
        rx.cond(
            WorkflowState.work_title == "",
            rx.heading(
                "Новый документ",
                class_name="text-xl tracking-[-0.055em] text-left font-bold font-manrope",
            ),
            rx.vstack(
                rx.heading(
                    WorkflowState.work_title,
                    class_name="text-xl font-semibold font-manrope",
                    padding_left="2em",
                    padding_right="2em",
                ),
                rx.cond(
                    WorkflowState.mode == "course",
                    rx.hstack(
                        rx.button(
                            "Начать заново",
                            on_click=WorkflowState.delete_work_title,
                            background_color=rx.color("gray", 12),
                        ),
                        rx.button(
                            "Остановить",
                            on_click=WorkflowState.stop_workflow,
                            background_color=rx.color("gray", 12),
                        ),
                        width="100%",
                        justify="center",
                    ),
                ),
                align="center",
                width="100%",
            ),
        ),
        rx.form.root(
            rx.hstack(
                rx.cond(
                    WorkflowState.mode == "course",
                    rx.input(
                        name="title",
                        placeholder="Введите тему работы...",
                        type="text",
                        required=True,
                        disabled=WorkflowState.is_processing,
                        width="100%",
                        max_length=255,
                    ),
                    rx.input(
                        name="title",
                        placeholder="Введите свой запрос...",
                        type="text",
                        required=True,
                        disabled=WorkflowState.is_processing,
                        width="100%",
                    ),
                ),
                rx.cond(
                    WorkflowState.is_processing,
                    rx.button(
                        "Начать",
                        type="submit",
                        disabled=True,
                        background_color=rx.color("gray", 1),
                    ),
                    rx.button(
                        "Начать",
                        type="submit",
                        disabled=False,
                        background_color=rx.color("gray", 12),
                    ),
                ),
                width="100%",
            ),
            on_submit=WorkflowState.set_work_title,
            reset_on_submit=True,
            width="100%",
            padding_left="50px",
            padding_right="50px",
        ),
        # Live updating chat history
        rx.vstack(
            rx.cond(
                WorkflowState.mode == "course",
                rx.scroll_area(
                    rx.foreach(
                        WorkflowState.chat_history,
                        lambda message: rx.box(
                            rx.hstack(
                                rx.markdown(
                                    message[0],
                                    class_name="font-medium font-manrope text-lg",
                                ),
                                rx.button(
                                    "Копировать",
                                    on_click=rx.set_clipboard(message[1]),
                                    size="1",
                                    variant="soft",
                                    color_scheme="gray",
                                    high_contrast=True,
                                    radius="large",
                                ),
                                align="center",
                                justify="between",
                            ),
                            rx.cond(
                                message[1] == "Генерация...",
                                rx.hstack(),
                                rx.vstack(
                                    rx.markdown(
                                        message[1],
                                        class_name="text-[13px] font-manrope font-regular",
                                    ),
                                    align="center",
                                ),
                            ),
                            padding_right="3em",
                            padding_left="3em",
                        ),
                    ),
                    type="scroll",
                    scrollbars="vertical",
                    style={"height": "30em"},
                ),
                rx.scroll_area(
                    rx.foreach(
                        WorkflowState.chat_history,
                        lambda message: rx.box(
                            rx.hstack(
                                rx.markdown(
                                    message[0],
                                    class_name="font-medium font-manrope text-lg",
                                ),
                                rx.button(
                                    "Копировать",
                                    on_click=rx.set_clipboard(message[1]),
                                    size="1",
                                    variant="soft",
                                    color_scheme="gray",
                                    high_contrast=True,
                                    radius="large",
                                ),
                                align="center",
                                justify="between",
                            ),
                            rx.cond(
                                message[1] == "Генерация...",
                                rx.hstack(
                                    rx.spinner(size="3"),
                                    rx.text(
                                        message[1],
                                        class_name="font-regular font-manrope text-[13px]",
                                    ),
                                ),
                                rx.markdown(
                                    message[1],
                                    class_name="text-[13px] font-regular font-manrope",
                                ),
                            ),
                            padding_right="3em",
                            padding_left="3em",
                        ),
                    ),
                    type="scroll",
                    scrollbars="vertical",
                    style={"height": "32em"},
                ),
            ),
            width="100%",
            spacing="0",
            height="100%",
        ),
        align="center",
        margin_top="1rem",
        width="100%",
        spacing="4",
    )
