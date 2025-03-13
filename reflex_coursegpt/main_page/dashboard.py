import reflex as rx
from .dashboard_components.leftbar import left_sidebar

from .dashboard_components.maincontent import main_content
from .dashboard_components.rightbar import right_sidebar
from .dashboard_components.header import header


@rx.page(route="/dashboard")
def dashboard() -> rx.Component:
    # Right Sidebar: Settings panel.
    # Assemble the three-panel layout.
    return rx.hstack(
        rx.vstack(
            header(),
            rx.hstack(
                left_sidebar(),
                main_content(),
                right_sidebar(),
                width="100%",
                height="100%",
            ),
            height="100%",
            width="100%",
            spacing="0",
        ),
        class_name="flex h-screen bg-background",
    )
