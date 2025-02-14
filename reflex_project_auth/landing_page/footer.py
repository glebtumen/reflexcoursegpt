import reflex as rx


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer() -> rx.Component:
    return rx.el.footer(
        rx.hstack(
            rx.vstack(
                rx.divider(),
                rx.hstack(
                    footer_item("Оферта", "/#"),
                    footer_item("Terms of Service", "/#"),
                    rx.flex(
                        rx.link(rx.icon("send"), rx.text("telegram"), href="/#"),
                    ),
                    spacing="4",
                    justify="between",
                    align_items="center",
                    width="100%",
                    padding_left="50px",
                    padding_right="50px",
                ),
                padding="25px",
                width="100%",
            )
        ),
        width="100%",
    )
