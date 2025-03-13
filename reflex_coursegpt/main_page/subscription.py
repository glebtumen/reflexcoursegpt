import reflex as rx

from ..base_state import State
from ..auth.login import require_login


class SubscriptionState(rx.State):
    base_price: int = 499
    points: str = "2"
    off: float = 0.8

    @rx.event
    def on_points_change(self, value: str) -> None:
        self.points = value

    @rx.event
    def on_submit(self, form_data: dict) -> None:
        print(form_data, self.points)


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(placeholder=placeholder, type=type, required=True),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def right_panel() -> rx.Component:
    return (
        rx.vstack(
            rx.hstack(
                rx.icon(
                    tag="key-round",
                    size=52,
                    color=rx.color("slate", 12),
                ),
                rx.vstack(
                    rx.text(
                        "Оформление доступа",
                        class_name="text-md font-bold font-manrope",
                    ),
                    rx.text(
                        'Заполни email, выбери количество недель и нажми "оформить"',
                        class_name="text-md font-medium font-manrope",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Email - отправим сюда чек",
                            "user@mail.ru",
                            "email",
                            "email",
                        ),
                        rx.text(
                            "Количество недель",
                            class_name="text-sm font-bold leading-9 font-manrope",
                        ),
                        rx.select.root(
                            rx.select.trigger(
                                width="100%",
                            ),
                            rx.select.content(
                                rx.select.item(
                                    f"1 неделя - {SubscriptionState.base_price} руб.",
                                    value="1",
                                ),
                                rx.select.item(
                                    f"2 недели - {SubscriptionState.base_price*2} руб.",
                                    value="2",
                                ),
                                rx.select.item(
                                    f"1 месяц - {SubscriptionState.base_price*5} руб.",
                                    value="5",
                                ),
                                rx.select.item(
                                    f"3 месяца - {SubscriptionState.base_price*15*SubscriptionState.off} руб. (скидка {100-SubscriptionState.off*100}%)",
                                    value="15",
                                ),
                                rx.select.item(
                                    f"1 год - {SubscriptionState.base_price*20*SubscriptionState.off} руб. (скидка {100-SubscriptionState.off*100}%)",
                                    value="54",
                                ),
                            ),
                            default_value="2",
                            on_change=SubscriptionState.on_points_change,
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                        ],
                    ),
                    rx.form.submit(
                        rx.button("Оформить"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=SubscriptionState.on_submit,
                reset_on_submit=False,
            ),
            width="48%",
            direction="column",
            spacing="4",
            align="start",
            justify="start",
            padding="20px",
            margin="3em",
            class_name="border-2 border-black shadow-[0_6px_0_0_black] p-4 rounded-lg bg-white",
        ),
    )


# return rx.vstack(
#     rx.heading("Subscription Plan", font_size="2em"),
#     rx.text("Price: $9.99 / month"),
#     rx.text("Features:"),
#     rx.unordered_list(
#         rx.list_item("Access to premium content"),
#         rx.list_item("Ad-free experience"),
#         rx.list_item("Monthly newsletter"),
#     ),
#     # rx.cond(
#     #     State.is_hydrated & State.token_is_valid,
#     #     rx.text(f"User Email: {State.user_email} User ID: {State.user_id}"),
#     #     rx.text("No email"),
#     # ),
#     rx.link("Subscribe Now", href="/", padding_top="1em"),
# )


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
                class_name="rounded-[100px] px-[15px] py-[1.5px] bg-[#1c2024] justify-center",
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
                rx.text("₽499", class_name="font-extrabold font-manrope text-[52px]"),
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
            rx.text(
                "Оформи доступ",
                class_name="text-md font-semibold font-manrope text-white",
            ),
            rx.icon("move-right", size=40, stroke_width=1, color="white"),
            width="100%",
            align="center",
            justify="center",
            background="#262626",
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
            ),
            align="start",
        ),
        align="start",
        justify="start",
        width="48%",
        padding="20px",
        margin="3em",
        class_name="border-2 border-black shadow-[0_6px_0_0_black] p-4 rounded-lg bg-white",
    )


@rx.page(route="/subscribe")
@require_login
def subscription_page() -> rx.Component:
    return rx.hstack(
        subscription_card(),
        right_panel(),
        class_name="bg-background",
    )
