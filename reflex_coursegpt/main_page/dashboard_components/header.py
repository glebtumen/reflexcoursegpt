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
                rx.text("КурсачГПТ", class_name="text-xl font-medium font-manrope"),
                rx.hover_card.root(
                    rx.hover_card.trigger(
                        rx.icon("circle-help", class_name="w-5 h-5"),
                    ),
                    rx.hover_card.content(
                        rx.text(
                            "Чтобы делать несколько работ одновременно - скопируй ссылку этой страницы и вставь в новых вкладках",
                            class_name="text-[13px] font-medium font-manrope",
                        ),
                    ),
                ),
                align="center",
                min_width="150px",
                margin_left="1em",
            ),
            # Right part: Access information and help.
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.html(
                            "Техподдержка",
                            class_name="text-black text-[13px] font-medium font-manrope",
                        ),
                        href="https://t.me/wlzeusgod",
                    ),
                    rx.cond(
                        False,
                        rx.link(
                            rx.html(
                                "Доступ до: 25.06.2025",
                                class_name="text-[#f0b41b] text-[13px] font-medium font-manrope",
                            ),
                            href="/subscribe",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.html(
                                    "<u>Нет доступа</u>",
                                    class_name="text-[#f0b41b] text-[13px] font-medium font-manrope",
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
