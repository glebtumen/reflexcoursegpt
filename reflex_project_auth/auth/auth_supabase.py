"""App module to demo authentication with supabase."""

import reflex as rx

from ..base_state import State
from ..auth.registration import registration_page as registration_page
from ..auth.login import require_login


def show_logout_or_login_comp() -> rx.Component:
    return rx.cond(
        State.is_hydrated & State.token_is_valid,
        rx.box(
            rx.link("Protected Page", href="/protected", padding_right="10px"),
            rx.link("Logout", href="/", on_click=State.do_logout),
            spacing="1.5em",
            padding_top="10%",
        ),
        rx.box(
            rx.link("Register", href="/register", padding_right="10px"),
            rx.link("Login", href="/login"),
            spacing="1.5em",
            padding_top="10%",
        ),
    )


def index() -> rx.Component:
    """Render the index page.

    Returns:
        A reflex component.
    """
    return rx.fragment(
        rx.vstack(
            rx.heading("Welcome to my homepage!", font_size="2em"),
            show_logout_or_login_comp(),
        )
    )


@require_login
def protected() -> rx.Component:
    """Render a protected page.

    The `require_login` decorator will redirect to the login page if the user is
    not authenticated.

    Returns:
        A reflex component.
    """
    return rx.vstack(
        rx.heading("Protected Page", font_size="2em"),
        rx.link("Home", href="/"),
        rx.link("Logout", href="/", on_click=State.do_logout),
    )


# app = rx.App()
# app.add_page(index)
# app.add_page(protected)
