import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            class_name="text-black font-manrope text-[15px] tracking-[-0.01em] font-regular",
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
                        class_name="text-xl font-manrope font-extrabold tracking-[-0.055em]",
                    ),
                    rx.hstack(
                        navbar_link("Цены", "/#price"),
                        navbar_link("FAQ", "/#faq"),
                        navbar_link("Поддержка", "https://t.me/wlzeusgod"),
                        align_items="center",
                        margin="20px",
                        margin_left="55px",
                    ),
                    align="center",
                ),
                rx.button(
                    "Вход",
                    href="/login",
                    class_name="text-white text-[15px] tracking-[-0.035em] font-regular font-manrope rounded px-4 py-4 bg-[#212227]",
                    width="70px",
                ),
                justify="between",
                align_items="center",
                margin_right="55px",
                margin_left="55px",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "КурсачГПТ",
                        class_name="text-[35px] font-manrope font-extrabold tracking-[-0.055em]",
                    ),
                    align_items="center",
                    margin="20px",
                ),
                rx.button(
                    "Вход",
                    href="/login",
                    class_name="text-white text-[15px] tracking-[-0.035em] font-regular font-manrope rounded px-4 py-4 bg-[#212227]",
                    width="70px",
                ),
                justify="between",
                align_items="center",
                margin_right="20px",
            ),
        ),
        class_name="border-b",
        top="35px",
        z_index="5",
        width="100%",
        background="white",
    )
