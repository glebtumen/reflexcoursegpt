import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            class_name="font-manrope text-black text-xl tracking-[-0.01em] font-medium",
        ),
        href=url,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "КурсачГПТ",
                        class_name="text-black text-[35px] font-manrope font-extrabold tracking-[-0.055em]",
                    ),
                    align_items="center",
                    margin="20px",
                    margin_left="55px",
                ),
                rx.hstack(
                    navbar_link("Цены", "/#"),
                    navbar_link("FAQ", "/#"),
                    navbar_link("Поддержка", "/#"),
                    rx.button(
                        "Вход",
                        href="/login",
                        class_name="text-white text-[17.7px] tracking-[-0.035em] font-medium font-manrope rounded-[47px] px-6 py-6 bg-[#212227]",
                    ),
                    spacing="5",
                    align="center",
                ),
                justify="between",
                align_items="center",
                margin_right="55px",
                padding="25px",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "КурсачГПТ",
                        class_name="text-black text-[35px] font-manrope font-extrabold tracking-[-0.055em]",
                    ),
                    align_items="center",
                    margin="20px",
                ),
                rx.button(
                    "Вход",
                    href="/login",
                    class_name="text-white text-[17.7px] tracking-[-0.035em] font-medium font-manrope rounded-[47px] px-6 py-6 bg-[#212227]",
                ),
                justify="between",
                align_items="center",
                margin_right="20px",
            ),
        ),
        class_name="shadow-[0px_4px_10px_0px_#f0f0f0]",
        top="35px",
        # z_index="5",
        width="100%",
    )
