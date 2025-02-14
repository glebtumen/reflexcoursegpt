"""App module to demo authentication with supabase."""

import reflex as rx

from .base_state import State
from .auth.registration import registration_page as registration_page
from .auth.login import require_login
from .auth.reset_password import reset_password_page
from .landing_page.landing_page import landing_page
from .main_page.subscription import subscription_page
from .main_page.help import help_page
from .main_page.dashboard import dashboard


def show_logout_or_login_comp() -> rx.Component:
    return rx.vstack(
        rx.heading("Main App Page", font_size="2em"),
        rx.cond(
            State.is_paid,
            rx.text("Subscription Status: Premium Subscriber"),
            rx.vstack(
                rx.text("Subscription Status: Not Paid"),
                rx.link("Subscribe Now", href="/subscribe"),
            ),
        ),
        rx.link("Logout", href="/", on_click=State.do_logout),
    )


@rx.page(route="/")
@require_login
def index() -> rx.Component:
    """Render the index page.

    Returns:
        A reflex component.
    """
    return rx.fragment(
        rx.vstack(
            rx.heading("Welcome to my homepage!", font_size="2em"),
            show_logout_or_login_comp(),
        ),
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&family=Roboto&display=swap",
    ],
)
app.add_page(index)
app.add_page(reset_password_page)
app.add_page(landing_page)
app.add_page(subscription_page)
app.add_page(help_page)
app.add_page(dashboard)
