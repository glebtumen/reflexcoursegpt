"""Reset password page for Reflex Project Auth.

Flows:
1. Send reset email.
2. Update password using tokens from the URL fragment.
"""

import reflex as rx
from ..auth.supabase__client import supabase_client
from ..base_state import State
from reflex.event import EventSpec
from typing import Generator
import logging
from urllib.parse import parse_qs

RESET_ROUTE = "/reset-password"


class ResetPasswordState(State):
    error: str = ""
    loading: bool = False
    reset_sent_success: bool = False
    success: bool = False

    def get_tokens_from_url(self) -> tuple:
        """Extract access and refresh tokens from the URL fragment."""
        url = self.router.page.raw_path
        if "#" in url:
            fragment = url.split("#", 1)[1]
            params = parse_qs(fragment)
            access_token = params.get("access_token", [None])[0]
            refresh_token = params.get("refresh_token", [None])[0]
            return access_token, refresh_token
        raise Exception("No URL fragment found for tokens")

    def send_reset_email(self, form_data) -> Generator[None, EventSpec | None, None]:
        self.loading = True
        yield
        try:
            supabase_client().auth.reset_password_for_email(
                form_data["email"],
                {
                    "redirect_to": "http://localhost:3123/reset-password?update=true",
                },
            )
            self.reset_sent_success = True
            self.error = ""
            logging.info("Reset email sent to %s", form_data.get("email", "unknown"))
        except Exception as e:
            self.error = "Failed to send reset email."
            logging.error("Send reset email error: %s", e)
        self.loading = False
        yield

    def update_password(self, form_data) -> Generator[None, EventSpec | None, None]:
        self.loading = True
        yield

        if form_data["new_password"] != form_data["confirm_password"]:
            self.error = "Passwords do not match."
            self.loading = False
            yield
            return

        try:
            access_token, refresh_token = self.get_tokens_from_url()
            if not access_token or not refresh_token:
                raise Exception("Missing required tokens")
            supabase_client().auth.set_session(access_token, refresh_token)
            supabase_client().auth.update_user({"password": form_data["new_password"]})
            self.success = True
            self.error = ""
            logging.info("Password updated successfully.")
        except Exception as e:
            self.success = False
            self.error = f"Failed to update password: {str(e)}"
            logging.error("Update password error: %s", e)

        self.loading = False
        yield


@rx.page(route=RESET_ROUTE)
def reset_password_page() -> rx.Component:
    return rx.cond(
        ResetPasswordState.router.page.params,
        rx.fragment(
            rx.cond(
                ResetPasswordState.success,
                rx.text("Password updated successfully."),
                rx.vstack(
                    rx.cond(
                        ResetPasswordState.error != "",
                        rx.text(ResetPasswordState.error),
                    ),
                    rx.form(
                        rx.input(
                            placeholder="New password",
                            type="password",
                            name="new_password",
                        ),
                        rx.input(
                            placeholder="Confirm password",
                            type="password",
                            name="confirm_password",
                        ),
                        rx.button(
                            "Update Password",
                            type="submit",
                            is_loading=ResetPasswordState.loading,
                        ),
                        on_submit=ResetPasswordState.update_password,
                        width="80vw",
                    ),
                    padding_top="20px",
                ),
            )
        ),
        rx.fragment(
            rx.cond(
                ResetPasswordState.reset_sent_success,
                rx.text("Reset email sent. Check your inbox."),
                rx.vstack(
                    rx.cond(
                        ResetPasswordState.error != "",
                        rx.text(ResetPasswordState.error),
                    ),
                    rx.form(
                        rx.input(placeholder="Email", type="email", name="email"),
                        rx.button(
                            "Send Reset Email",
                            type="submit",
                            is_loading=ResetPasswordState.loading,
                        ),
                        on_submit=ResetPasswordState.send_reset_email,
                        width="80vw",
                    ),
                    padding_top="20px",
                ),
            )
        ),
    )
