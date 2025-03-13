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
                    class_name="font-regular font-manrope text-[15px] text-[#ffffff]",
                ),
                align="center",
                justify="center",
                class_name="rounded-[100px] px-[15px] py-[1.5px] bg-black justify-center",
            ),
            rx.hstack(
                rx.text(
                    "Особая цена!",
                    class_name="font-regular font-manrope text-[15px] text-[#ca3e41]",
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
                    rx.icon("send", size=40, stroke_width=1.5),
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
                "padding": "18px 18px",
                "border": "1px solid #ccc",
                "borderRadius": "15px",
                "cursor": "pointer",
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
                        "Вывод в файл Word",
                        class_name="text-md font-medium font-manrope",
                    ),
                    align="center",
                ),
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
                        "Генерация до 100 курсовых в неделю",
                        class_name="text-md font-medium font-manrope",
                    ),
                    align="center",
                ),
                rx.hstack(
                    rx.icon("check", size=25, stroke_width=1.5),
                    rx.text(
                        "Настройка креативности и детальности текста",
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
        width="600px",
        padding="20px",
        class_name="border-2 border-black shadow-[0_6px_0_0_black] p-4 rounded-lg bg-white",
    )


def main_content() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.vstack(
                rx.vstack(
                    background_v3(),
                    rx.image(
                        src="/screen1.png",
                        class_name="rounded-[18px] md:rounded-lg lg:rounded-lg border-[#212227] shadow-[0_6px_0_0_#212227]",
                        border_width="medium",
                    ),
                    spacing="8",
                    align="center",
                ),
                rx.vstack(
                    rx.html(
                        "Настраивай запросы<br>для каждой работы",
                        class_name="text-black text-4xl md:text-6xl lg:text-6xl tracking-[-0.055em] text-center font-extrabold font-manrope",
                    ),
                    rx.text(
                        "Три режима для удобной работы c курсовыми",
                        class_name=" text-[1.5rem] tracking-[-0.035em] text-center font-medium font-manrope",
                    ),
                    rx.hstack(
                        rx.image(
                            src="/screen1.png",
                            border_width="medium",
                            class_name="rounded-lg lg:h-[566px] lg:w-[419px] h-[380px] w-[300px] border-[#212227] shadow-[0_6px_0_0_#212227]",
                        ),
                        rx.image(
                            src="/screen1.png",
                            border_width="medium",
                            class_name="rounded-lg lg:h-[566px] lg:w-[419px] h-[380px] w-[300px] border-[#212227] shadow-[0_6px_0_0_#212227]",
                        ),
                        justify="center",
                        align="center",
                    ),
                    spacing="5",
                    align="center",
                    padding_top="55px",
                ),
                rx.vstack(
                    rx.html(
                        "Одна оплата —<br> неограниченное количество работ",
                        class_name="text-black text-2xl md:text-4xl lg:text-5xl tracking-[-0.055em] text-center font-extrabold font-manrope",
                    ),
                    subscription_card(),
                    id="price",
                    spacing="5",
                    align="center",
                    margin="3em",
                ),
                rx.vstack(
                    rx.html(
                        "Часто задаваемые вопросы",
                        class_name="text-black text-left text-5xl tracking-[-0.055em] font-extrabold font-manrope",
                    ),
                    align="center",
                    margin_top="3em",
                    id="faq",
                ),
                faq_v1(),
                spacing="8",
                margin_right="100px",
                margin_left="100px",
                margin_top="10px",
                align="center",
            ),
        ),
        spacing="9",
        padding="8",
        class_name="bg-white",
        align="center",
    )
