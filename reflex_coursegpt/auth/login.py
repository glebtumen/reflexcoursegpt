"""Login page and authentication logic."""

import reflex as rx

from ..base_state import State
from .supabase__client import supabase_client
from reflex.event import EventSpec
from typing import Generator

LOGIN_ROUTE = "/login"
REGISTER_ROUTE = "/register"
import logging

logging.basicConfig(level=logging.INFO)


class LoginState(State):
    """Handle login form submission and redirect to proper routes after authentication."""

    error_message: str = ""
    redirect_to: str = ""

    is_loading: bool = False

    def get_current_page(self) -> str:
        """Get the current page route."""
        return self.router.page.path  # Accessing the current page route from the router

    def on_submit(self, form_data) -> Generator[None, EventSpec | None, None]:
        """Handle login form on_submit.

        Args:
            form_data: A dict of form fields and values.
        """

        logging.info(f"Form data received: {form_data}")  # Log form data
        # set the following values to spin the button
        self.is_loading = True
        yield

        self.error_message = ""
        email = form_data["email"]
        password = form_data["password"]

        try:
            user_sign_in = supabase_client().auth.sign_in_with_password(
                {"email": email, "password": password}
            )
            logging.info(
                f"User signed in successfully: {user_sign_in.user.email}"
            )  # Log successful sign-in
            self.auth_token = user_sign_in.session.access_token
            self.error_message = ""
            return LoginState.redir()  # type: ignore
        except Exception as e:
            self.error_message = "There was a problem logging in, please try again."
            logging.error(f"Error during sign-in: {e}")  # Log error message

            # reset state variable again
            self.is_loading = False
            yield

    def redir(self) -> Generator[None, None, EventSpec | None]:
        """Redirect to the redirect_to route if logged in, or to the login page if not."""
        logging.info(f"Hydration state: {self.is_hydrated}")  # Log hydration state
        if not self.is_hydrated:
            # wait until after hydration
            return LoginState.redir()  # type: ignore
        page = self.get_current_page()
        logging.info(f"Current page: {page}")  # Log current page

        if not self.token_is_valid and page != LOGIN_ROUTE:
            self.redirect_to = page

            logging.info(
                f"Redirecting to LOGIN_ROUTE: {LOGIN_ROUTE}"
            )  # Log redirection
            # reset state variable again
            self.is_loading = False
            yield

            return rx.redirect(LOGIN_ROUTE)
        elif page == LOGIN_ROUTE:

            logging.info(
                f"Redirecting to: {self.redirect_to or '/'}"
            )  # Log redirection
            # reset state variable again
            self.is_loading = False
            yield

            return rx.redirect(self.redirect_to or "/")


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


def login_panel() -> rx.Component:
    return (
        rx.vstack(
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Email",
                            "user@mail.ru",
                            "email",
                            "email",
                        ),
                        form_field(
                            "Password",
                            "***",
                            "password",
                            "password",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                        ],
                    ),
                    rx.form.submit(
                        rx.button("Войти", is_loading=LoginState.is_loading),
                        rx.button("Войти", is_loading=True),
                        as_child=True,
                    ),
                    rx.link(rx.text("Регистрация"), href=REGISTER_ROUTE),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=LoginState.on_submit,
                reset_on_submit=False,
            ),
            width="48%",
            min_width="300px",
            max_width="400px",
            direction="column",
            spacing="4",
            align="start",
            justify="start",
            padding="20px",
            margin="3em",
            class_name="border-2 border-black shadow-[0_6px_0_0_black] p-4 rounded-lg bg-white",
        ),
    )


def login_panel2() -> rx.Component:
    return rx.vstack(
        rx.html(
            "Вход в КурсачГПТ",
            class_name=" text-6xl md:text-8xl lg:text-8xl tracking-[-0.055em] text-center text-black font-extrabold font-manrope",
            margin_top="30px",
        ),
        login_panel(),
        width="100%",
        height="100%",
        align="center",
    )


@rx.page(route=LOGIN_ROUTE)
def login_page() -> rx.Component:
    """Render the login page."""

    return rx.fragment(
        rx.cond(
            LoginState.is_hydrated,  # type: ignore
            rx.vstack(
                rx.cond(  # conditionally show error messages
                    LoginState.error_message != "",
                    rx.text(LoginState.error_message),
                ),
                login_panel2(),
                align="center",
                justify="center",
                background_size="100px 100px",
                background_image="linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)",
                height="100vh",
            ),
        ),
        align="center",
    )


def require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    """Decorator to require authentication before rendering a page.

    If the user is not authenticated, then redirect to the login page.

    Args:
        page: The page to wrap.

    Returns:
        The wrapped page component.
    """

    def protected_page():
        return rx.fragment(
            rx.cond(
                State.is_hydrated,
                rx.cond(State.token_is_valid, page(), login_page()),
                rx.center(
                    # When this spinner mounts, it will redirect to the login page
                    rx.spinner(),
                ),
            )
        )

    protected_page.__name__ = page.__name__
    return protected_page
