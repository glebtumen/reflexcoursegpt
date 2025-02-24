import reflex as rx


def header() -> rx.Component:
    return (
        rx.hstack(
            # Left part: Logo and title.
            rx.hstack(
                rx.image(
                    src="/logo.jpg",
                    alt="Logo",
                    class_name="w-10 h-10",
                ),
                rx.text("КурсачГПТ", class_name="text-lg font-medium font-manrope"),
                align="center",
                min_width="150px",
            ),
            # Right part: Access information and help.
            rx.hstack(
                rx.vstack(
                    rx.cond(
                        False,
                        rx.link(
                            rx.html(
                                "<u>Доступ до: 25.06.2025</u>",
                                class_name="text-[#f0b41b]",
                            ),
                            href="/subscribe",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.html(
                                    "<u>Нет доступа</u>",
                                    class_name="text-[#f0b41b]",
                                ),
                                href="/subscribe",
                            ),
                            align="center",
                        ),
                    ),
                    margin_right="1em",
                ),
                rx.button(
                    rx.icon("log-out", class_name="w-5 h-5"),
                    color=rx.color("slate", 12),
                    background="white",
                ),
                align="center",
                margin_right="1em",
                spacing="3",
            ),
            justify="between",
            align_items="center",
            class_name="border-b",
            min_height="70px",
            width="100%",
        ),
    )
