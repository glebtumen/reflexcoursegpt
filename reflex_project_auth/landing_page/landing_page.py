import reflex as rx
from .navbar import navbar
from .main_content import main_content
from .responsive_landing import responsive_main_content
from .footer import footer


def landing_page() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.tablet_and_desktop(main_content()),
        rx.mobile_only(
            responsive_main_content(),
            width="340px",
        ),
        rx.box(
            "",
            class_name="absolute inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)] z-0",
            height="105vh",
        ),
        footer(),
        spacing="2",
        align="center",
        width="100%",
    )
