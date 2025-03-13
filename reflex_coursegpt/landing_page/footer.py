import reflex as rx
from reflex.constants.colors import Color
from dataclasses import dataclass, field

active: Color = rx.color("slate", 12)
passive: Color = rx.color("slate", 10)


@dataclass
class FooterV2Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "20vh",
            "align": "center",
            "justify": "center",
            "padding": "0em 1em",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "justify": "between",
            "align": "center",
            "padding": "1em 2em",
        },
    )

    link: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "weight": "medium",
            "size": "2",
        },
    )

    brand: dict[str, str] = field(
        default_factory=lambda: {
            "weight": "medium",
        },
    )


def media(name: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterV2Style().link), href="#")


def footer() -> rx.Component:
    return rx.vstack(
        rx.divider(olor=rx.color("slate", 11)),
        rx.hstack(
            rx.text("КурсачГПТ 2025", **FooterV2Style().brand),
            rx.hstack(media("Оферта")),
            rx.hstack(media("Telegram")),
            **FooterV2Style().content,
        ),
        **FooterV2Style().base,
    )
