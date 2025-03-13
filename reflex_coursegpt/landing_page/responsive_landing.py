import reflex as rx
from .faq import faq_v1
from .background_v3 import background_v3

import reflex as rx


def subscription_card() -> rx.Component:
    return rx.vstack(
        # Top row with options.
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Скидка до конца месяца",
                    class_name="font-regular font-manrope text-[12px] text-[#ffffff]",
                ),
                align="center",
                justify="center",
                class_name="rounded-[100px] px-[15px] py-[1.5px] bg-black justify-center",
            ),
            rx.hstack(
                rx.text(
                    "Особая цена!",
                    class_name="font-regular font-manrope text-[12px] text-[#ca3e41]",
                ),
                align="center",
                justify="center",
                class_name="rounded-[100px] px-[15px] py-[1.5px] justify-center",
                background="#ffe3e3",
            ),
            align="center",
            justify="start",
        ),
        # Price and description.
        rx.vstack(
            rx.hstack(
                rx.text(
                    "₽499",
                    class_name="text-black font-extrabold font-manrope text-[52px]",
                ),
                rx.text(
                    "/неделя",
                    class_name="font-medium font-manrope text-[22px]",
                    color="#828282",
                ),
                align="baseline",
                spacing="0",
            ),
            rx.text(
                "Пиши студенческие работ за минуты, a не часы.",
                class_name="text-md font-semibold font-manrope",
                color="#828282",
            ),
            rx.text(
                "Идеально для фрилансеров, работающих c курсовыми, дипломными и рефератами",
                class_name="text-md font-semibold font-manrope",
            ),
            padding_y="2",
        ),
        rx.vstack(
            rx.hstack(
                rx.image(src="/avatar.png", class_name="w-12 h-12"),
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Есения", class_name="text-md font-semibold font-manrope"
                        ),
                        rx.link(
                            rx.text("t.me/courseGPTproof/47"),
                            href="t.me/courseGPTproof/47",
                            class_name="font-regular font-manrope text-[#828282]",
                        ),
                        spacing="0",
                    ),
                    width="100%",
                    align="center",
                    justify="between",
                ),
                width="100%",
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "Пользуюсь разными ботами уже третий год, пишу работы на заказ уже два года, но когда нашла этот бот не стала даже делиться им с кем-то, вдруг кто-то из моего универа найдёт это сокровище и заберёт мой доход...",
                    class_name="text-md font-semibold font-manrope",
                ),
                align="center",
            ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "15px",
                "cursor": "pointer",
                "padding": "18px",
            },
        ),
        # Call-to-action button.
        rx.hstack(
            rx.link(
                rx.text(
                    "Оформи доступ",
                    class_name="text-md font-semibold font-manrope text-white",
                ),
                href="/login",
                class_name="text-white",
            ),
            rx.icon("move-right", size=40, stroke_width=1, color="white"),
            width="100%",
            align="center",
            justify="center",
            background="black",
            class_name="rounded-[12px]",
        ),
        # Features list.
        rx.vstack(
            rx.text(
                "Возможности :",
                class_name="text-md font-bold font-manrope",
            ),
            rx.vstack(
                rx.hstack(
                    rx.icon("check", size=25, stroke_width=1.5),
                    rx.text(
                        "До 10 курсовых одновременно",
                        class_name="text-md font-medium font-manrope",
                    ),
                    align="center",
                ),
                rx.hstack(
                    rx.icon("check", size=25, stroke_width=1.5),
                    rx.text(
                        "Поиск источников в интернете",
                        class_name="text-md font-medium font-manrope",
                    ),
                    align="center",
                ),
                rx.hstack(
                    rx.icon("check", size=25, stroke_width=1.5),
                    rx.text(
                        "Настройка детальности текста",
                        class_name="text-md font-medium font-manrope",
                    ),
                    align="center",
                ),
                rx.hstack(
                    rx.icon("check", size=25, stroke_width=1.5),
                    rx.text(
                        "Генерация вопросов для защиты",
                        class_name="text-md font-medium font-manrope",
                    ),
                    align="center",
                ),
                spacing="3",
                align="start",
                justify="start",
            ),
            align="start",
            justify="start",
        ),
        align="start",
        justify="start",
        width="100%",
        class_name="border-2 border-black shadow-[0_6px_0_0_black] p-4 rounded-lg bg-white",
    )


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


def responsive_main_content() -> rx.Component:
    return (
        rx.vstack(
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.vstack(
                            rx.html(
                                "Делай курсовые мгновенно<br>с помощью ИИ",
                                class_name=" text-[3rem] tracking-[-0.055em] text-center text-black font-extrabold font-manrope",
                                line_height="3rem",
                            ),
                            rx.html(
                                "Детальные настройки, поиск в интернете, создавай несколько курсовых одновременно.<br>Не теряй времени!",
                                class_name=" text-[1.3rem] tracking-[-0.035em] text-center font-medium font-manrope",
                            ),
                            input_field(),
                            # mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0.7))",
                            spacing="8",
                            align="center",
                            width="340px",
                        ),
                        class_name="relative z-10",
                        height="55vh",
                    ),
                    class_name="relative",
                    margin_top="55px",
                ),
                rx.image(
                    src="/screen1.png",
                    class_name="rounded-[18px] rounded-lg w-[330px] border-[#212227] shadow-[0_6px_0_0_#212227]",
                    border_width="medium",
                    margin_top="20px",
                ),
                spacing="8",
                align="center",
            ),
            rx.vstack(
                rx.html(
                    "Настраивай запросы<br>для каждой работы",
                    class_name="text-black text-4xl md:text-6xl lg:text-6xl tracking-[-0.055em] text-center font-extrabold font-manrope",
                ),
                rx.image(
                    src="/screen1.png",
                    border_width="medium",
                    class_name="rounded-lg w-[330px] border-[#212227] shadow-[0_6px_0_0_#212227]",
                ),
                rx.text(
                    "Три режима для удобной работы c курсовыми",
                    class_name="text-black text-4xl md:text-6xl lg:text-6xl tracking-[-0.055em] text-center font-extrabold font-manrope",
                ),
                rx.image(
                    src="/screen1.png",
                    border_width="medium",
                    class_name="rounded-lg w-[330px] border-[#212227] shadow-[0_6px_0_0_#212227]",
                ),
                spacing="5",
                align="center",
            ),
            rx.vstack(
                rx.html(
                    "Одна оплата —<br> неограниченное количество работ",
                    class_name="text-black text-4xl md:text-6xl lg:text-6xl tracking-[-0.055em] text-center font-extrabold font-manrope",
                ),
                subscription_card(),
                id="price",
                spacing="5",
                align="center",
            ),
            rx.vstack(
                rx.html(
                    "Часто задаваемые вопросы",
                    class_name="text-black text-left text-5xl tracking-[-0.055em] font-extrabold font-manrope",
                ),
                align="center",
                id="faq",
            ),
            faq_v1(),
            spacing="8",
            margin_top="10px",
            align="center",
            class_name="bg-white",
        ),
    )
