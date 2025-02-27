import reflex as rx


def input_field() -> rx.Component:
    return rx.hstack(
        rx.input(
            name="title",
            placeholder="Введи тему своей курсовой...",
            type="text",
            disabled=False,
            required=False,
            width="400px",
            max_length=255,
            variant="soft",
            color_scheme="gray",
            class_name="font-manrope font-bold text-[15px] tracking-[-0.035em] text-black",
            size="2",
        ),
        rx.button(
            rx.icon("wand-sparkles", size=15),
            disabled=False,
            class_name="relative rounded px-5 py-2.5 overflow-hidden group bg-[#1B1B1B] relative hover:bg-gradient-to-r hover:from-[#1B1B1B] hover:to-[#565656] text-white hover:ring-2 hover:ring-offset-2 hover:ring-[#565656] transition-all ease-out duration-300",
            width="70px",
        ),
        align="center",
        justify="center",
        gap="1",
        width="100%",
    )


def background_v3():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.html(
                    "Твой ИИ-помощник<br>для курсовых",
                    class_name=" text-[5.5rem] tracking-[-0.055em] text-center text-black font-extrabold font-manrope",
                    line_height="4.5rem",
                ),
                rx.html(
                    "Нужна только <u>тема работы</u>!",
                    class_name=" text-[1.5rem] tracking-[-0.035em] text-center font-medium font-manrope",
                ),
                input_field(),
                # mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0.7))",
                spacing="8",
                align="center",
            ),
            class_name="relative z-10",
            width="100%",
            height="55vh",
        ),
        class_name="relative",
        margin_top="55px",
    )
