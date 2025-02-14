import reflex as rx
from ..base_state import State
from ..auth.login import require_login


@rx.page(route="/subscribe")
@require_login
def subscription_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Subscription Plan", font_size="2em"),
        rx.text("Price: $9.99 / month"),
        rx.text("Features:"),
        rx.unordered_list(
            rx.list_item("Access to premium content"),
            rx.list_item("Ad-free experience"),
            rx.list_item("Monthly newsletter"),
        ),
        rx.cond(
            State.is_hydrated & State.token_is_valid,
            rx.text(f"User Email: {State.user_email} User ID: {State.user_id}"),
            rx.text("No email"),
        ),
        rx.link("Subscribe Now", href="/", padding_top="1em"),
    )
