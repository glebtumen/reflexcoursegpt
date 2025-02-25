import reflex as rx
from ..dashboard_state import WorkflowState


def custom_radio_group(options: list[tuple[str, str, str]]) -> rx.Component:
    """
    Render a simple custom radio item without interactive logic.
    Each option is a tuple of (label, value, description).
    """
    return rx.hstack(
        *[
            rx.box(
                rx.hstack(
                    # Always display the unselected icon.
                    # rx.cond(
                    #     WorkflowState.mode == value,
                    #     rx.icon("circle-check-big", size=60, stroke_width=2.5),
                    #     rx.icon("circle-dashed", size=60, stroke_width=2.5),
                    # ),
                    rx.vstack(
                        rx.text(label, class_name="font-bold font-manrope text-[13px]"),
                        rx.text(
                            desc,
                            class_name="text-[13px] font-regular text-black font-manrope",
                        ),
                        spacing="1",
                    ),
                    style={
                        "padding": "8px 12px",
                        "border": "1px solid #ccc",
                        "borderRadius": "8px",
                        "cursor": "pointer",
                        "backgroundColor": rx.cond(
                            WorkflowState.mode == value, "#F1F1F1", "#ffffff"
                        ),
                    },
                    class_name="custom-radio-item",
                    align="center",
                ),
                on_click=lambda v=value: WorkflowState.set_mode(v),
            )
            for label, value, desc in options
        ],
        spacing="4",
        flex_direction="column"
    )


def left_sidebar() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Режим",
            class_name="text-xl font-semibold font-manrope",
        ),
        rx.vstack(
            custom_radio_group(
                options=[
                    (
                        "Курсовая",
                        "course",
                        "В режиме курсовая можно написать курсовую работу, отправив лишь тему. Используйте настройки, чтобы получить более разнообразный текст",
                    ),
                    (
                        "Свободный режим",
                        "free",
                        "Свободный режим нужен для индивидуальный просьб (например, оформить источники). Работает, как обычный чат, задай вопрос - получи ответ",
                    ),
                ]
            ),
            spacing="4",
            height="100%",
        ),
        class_name="min-w-80 w-80 border-r p-4",
        height="100%",
    )
