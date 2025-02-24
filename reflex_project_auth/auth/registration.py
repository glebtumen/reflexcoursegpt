"""New user registration form and validation logic."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator
from reflex.event import EventSpec
import reflex as rx

# from ..removed.base_state import State
from .login import LOGIN_ROUTE, REGISTER_ROUTE
import re

# from ..auth.supabase__client import supabase_client


import logging

logging.basicConfig(level=logging.INFO)


# class RegistrationState(State):
#     """Handle registration form submission and redirect to login page after registration."""

#     success: bool = False
#     error_message: str = ""

#     is_loading: bool = False

#     async def handle_registration(
#         self, form_data
#     ) -> AsyncGenerator[EventSpec | list[EventSpec] | None, None]:
#         """Handle registration form on_submit.

#         Set error_message appropriately based on validation results.

#         Args:
#             form_data: A dict of form fields and values.
#         """

#         # set the following values to spin the button
#         self.is_loading = True
#         yield

#         email = form_data["email"]
#         if not email:
#             self.error_message = "email cannot be empty"
#             rx.set_focus("email")
#             # reset state variable again
#             self.is_loading = False
#             yield
#             return
#         if not is_valid_email(email):
#             self.error_message = "email is not a valid email address."
#             rx.set_focus("email")
#             # reset state variable again
#             self.is_loading = False
#             yield
#             return

#         password = form_data["password"]
#         if not password:
#             self.error_message = "Password cannot be empty"
#             rx.set_focus("password")
#             # reset state variable again
#             self.is_loading = False
#             yield
#             return
#         if password != form_data["confirm_password"]:
#             self.error_message = "Passwords do not match"
#             [
#                 rx.set_value("confirm_password", ""),
#                 rx.set_focus("confirm_password"),
#             ]
#             # reset state variable again
#             self.is_loading = False
#             yield
#             return

#         # sign up with supabase
#         supabase_client().auth.sign_up(
#             {
#                 "email": email,
#                 "password": password,
#             }
#         )

#         # Set success and redirect to login page after a brief delay.
#         self.error_message = ""
#         self.success = True
#         self.is_loading = False
#         yield
#         await asyncio.sleep(3)
#         yield [rx.redirect(LOGIN_ROUTE), RegistrationState.set_success(False)]


def reg_success() -> rx.Component:
    return (
        rx.vstack(
            rx.text(
                "Регистрация успешна, проверьте вашу почту, чтобы подтвердить регистрацию!"
            ),
            width="48%",
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


def reg_panel() -> rx.Component:
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
                        form_field(
                            "Confirm Password",
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
                        # rx.button("Регистрация", is_loading=LoginState.is_loading),
                        rx.button("Регистрация"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                # on_submit=RegistrationState.handle_registration,
                reset_on_submit=False,
            ),
            width="48%",
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


def reg_panel2() -> rx.Component:
    return rx.vstack(
        rx.html(
            "Регистрация в КурсачГПТ",
            class_name=" text-6xl md:text-8xl lg:text-8xl tracking-[-0.055em] text-center text-black font-extrabold font-manrope",
            margin_top="30px",
        ),
        reg_panel(),
        width="100%",
        height="100%",
        align="center",
    )


@rx.page(route=REGISTER_ROUTE)
def registration_page() -> rx.Component:
    """Render the registration page."""

    return rx.fragment(
        rx.cond(
            False,
            # RegistrationState.success,
            rx.vstack(
                reg_success(),
                rx.spinner(),
                align="center",
                justify="center",
            ),
            rx.vstack(
                # rx.cond(  # conditionally show error messages
                #     RegistrationState.error_message != "",
                #     rx.text(RegistrationState.error_message),
                # ),
                reg_panel2(),
                align="center",
                justify="center",
                background_size="100px 100px",
                background_image="linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)",
                height="100vh",
            ),
        )
    )


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None
