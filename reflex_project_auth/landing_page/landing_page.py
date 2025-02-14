import reflex as rx
from .navbar import navbar
from .main_content import main_content
from .footer import footer


@rx.page(route="/landing")
def landing_page() -> rx.Component:
    return rx.vstack(
        navbar(),
        main_content(),
        footer(),
        spacing="2",
        align="center",
    )
