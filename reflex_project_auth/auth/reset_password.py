"""Reset password page for Reflex Project Auth.

Flows:
1. Send reset email.
2. Update password using tokens from the URL fragment.
"""

import reflex as rx

# from ..auth.supabase__client import supabase_client
# from ..removed.base_state import State
from reflex.event import EventSpec
from typing import Generator
import logging
from urllib.parse import parse_qs

RESET_ROUTE = "/reset-password"


# class ResetPasswordState(State):
#     error: str = ""
#     loading: bool = False
#     reset_sent_success: bool = False
#     success: bool = False

#     def get_tokens_from_url(self) -> tuple:
#         """Extract access and refresh tokens from the URL fragment."""
#         url = self.router.page.raw_path
#         if "#" in url:
#             fragment = url.split("#", 1)[1]
#             params = parse_qs(fragment)
#             access_token = params.get("access_token", [None])[0]
#             refresh_token = params.get("refresh_token", [None])[0]
#             return access_token, refresh_token
#         raise Exception("No URL fragment found for tokens")

#     def send_reset_email(self, form_data) -> Generator[None, EventSpec | None, None]:
#         self.loading = True
#         yield
#         try:
#             supabase_client().auth.reset_password_for_email(
#                 form_data["email"],
#                 {
#                     "redirect_to": "http://localhost:3123/reset-password?update=true",
#                 },
#             )
#             self.reset_sent_success = True
#             self.error = ""
#             logging.info("Reset email sent to %s", form_data.get("email", "unknown"))
#         except Exception as e:
#             self.error = "Failed to send reset email."
#             logging.error("Send reset email error: %s", e)
#         self.loading = False
#         yield

#     def update_password(self, form_data) -> Generator[None, EventSpec | None, None]:
#         self.loading = True
#         yield

#         if form_data["new_password"] != form_data["confirm_password"]:
#             self.error = "Passwords do not match."
#             self.loading = False
#             yield
#             return

#         try:
#             access_token, refresh_token = self.get_tokens_from_url()
#             if not access_token or not refresh_token:
#                 raise Exception("Missing required tokens")
#             supabase_client().auth.set_session(access_token, refresh_token)
#             supabase_client().auth.update_user({"password": form_data["new_password"]})
#             self.success = True
#             self.error = ""
#             logging.info("Password updated successfully.")
#         except Exception as e:
#             self.success = False
#             self.error = f"Failed to update password: {str(e)}"
#             logging.error("Update password error: %s", e)

#         self.loading = False
#         yield


def reset_success() -> rx.Component:
    return (
        rx.vstack(
            rx.text("Пароль успешно обновлен, вы можете войти с новым паролем!"),
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


def reset_sent() -> rx.Component:
    return (
        rx.vstack(
            rx.text(
                "Отправлено письмо с ссылкой для сброса пароля, проверьте вашу почту!"
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


def new_password_panel() -> rx.Component:
    return (
        rx.vstack(
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "New password",
                            "***",
                            "password",
                            "password",
                        ),
                        form_field(
                            "Confirm password",
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
                        # rx.button("Войти", is_loading=LoginState.is_loading),
                        rx.button("Обновить пароль", is_loading=True),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                # on_submit=ResetPasswordState.update_password,
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


def new_password_email_panel() -> rx.Component:
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
                        spacing="3",
                        flex_direction=[
                            "column",
                        ],
                    ),
                    rx.form.submit(
                        # rx.button("Войти", is_loading=LoginState.is_loading),
                        rx.button("Восстановить пароль", is_loading=True),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                # on_submit=ResetPasswordState.send_reset_email,
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


@rx.page(route=RESET_ROUTE)
def reset_password_page() -> rx.Component:
    return rx.cond(
        False,
        # ResetPasswordState.router.page.params,
        rx.fragment(
            rx.cond(
                False,
                # ResetPasswordState.success,
                rx.vstack(
                    reset_success(),
                    align="center",
                    justify="center",
                ),
                rx.vstack(
                    # rx.cond(
                    #     ResetPasswordState.error != "",
                    #     rx.text(ResetPasswordState.error),
                    # ),
                    new_password_panel(),
                    align="center",
                    justify="center",
                    padding_top="20px",
                    background_size="100px 100px",
                    background_image="linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)",
                    height="100vh",
                ),
            )
        ),
        rx.fragment(
            rx.cond(
                False,
                # ResetPasswordState.reset_sent_success,
                rx.vstack(
                    reset_sent(),
                    align="center",
                    justify="center",
                ),
                rx.vstack(
                    # rx.cond(
                    #     ResetPasswordState.error != "",
                    #     rx.text(ResetPasswordState.error),
                    # ),
                    new_password_email_panel(),
                    align="center",
                    justify="center",
                    padding_top="20px",
                    background_size="100px 100px",
                    background_image="linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)",
                    height="100vh",
                ),
            )
        ),
    )
