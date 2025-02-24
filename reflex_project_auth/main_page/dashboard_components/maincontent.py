import reflex as rx
from ..dashboard_state import WorkflowState


def main_content() -> rx.Component:
    return rx.vstack(
        rx.cond(
            WorkflowState.work_title == "",
            rx.heading(
                "Новый документ", class_name="text-2xl font-semibold font-manrope"
            ),
            rx.vstack(
                rx.heading(
                    WorkflowState.work_title,
                    class_name="text-2xl font-semibold font-manrope",
                    padding_left="2em",
                    padding_right="2em",
                ),
                rx.hstack(
                    rx.button(
                        "Начать заново",
                        on_click=WorkflowState.delete_work_title,
                        class_name="font-light font-manrope rounded-3xl bg-white flex items-center border border-black-300 py-2 px-4 text-center transition-all shadow-sm hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 hover:border-slate-800 focus:text-white focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none",
                    ),
                    rx.button(
                        "Остановить",
                        on_click=WorkflowState.stop_workflow,
                        class_name="font-light font-manrope rounded-3xl bg-white flex items-center border border-black-300 py-2 px-4 text-center transition-all shadow-sm hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 hover:border-slate-800 focus:text-white focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none",
                    ),
                    width="100%",
                    justify="center",
                ),
                align="center",
                width="100%",
            ),
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="title",
                    placeholder="Введите тему работы...",
                    type="text",
                    required=True,
                    disabled=WorkflowState.is_processing,
                    width="100%",
                    max_length=100,
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
            rx.foreach(
                WorkflowState.chat_history,
                lambda message: rx.box(
                    rx.markdown(
                        message[0], class_name="text-lg font-manrope font-medium"
                    ),
                    rx.cond(
                        message[1] == "Генерация...",
                        rx.hstack(
                            rx.spinner(size="3"),
                            rx.text(
                                message[1], class_name="text-md font-manrope font-bold"
                            ),
                            padding="10px",
                        ),
                        rx.markdown(
                            message[1],
                            class_name="text-[14px] font-manrope font-medium",
                        ),
                    ),
                    padding_right="3em",
                    padding_left="3em",
                    margin_y="0.5em",
                ),
            ),
            width="100%",
        ),
        align="center",
        padding="4",
        width="100%",
        spacing="4",
    )
