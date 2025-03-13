import reflex as rx

from .base_state import State
from .auth.login import require_login
from .auth.registration import registration_page
from .auth.login import login_page
from .auth.reset_password import reset_password_page
from .landing_page.landing_page import landing_page

from .main_page.subscription import subscription_page
from .main_page.dashboard import dashboard
from .main_page.dashboard_state import WorkflowState


# def show_logout_or_login_comp() -> rx.Component:
#     return rx.vstack(
#         rx.heading("Main App Page", font_size="2em"),
#         rx.cond(
#             True,
#             rx.text("Subscription Status: Premium Subscriber"),
#             rx.vstack(
#                 rx.text("Subscription Status: Not Paid"),
#                 rx.link("Subscribe Now", href="/subscribe"),
#             ),
#         ),
#         # rx.link("Logout", href="/", on_click=State.do_logout),
#     )


@rx.page(route="/")
# @require_login
def index() -> rx.Component:
    return landing_page()


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&family=Roboto&display=swap",
    ],
)
app.add_page(index)
app.add_page(reset_password_page)
app.add_page(landing_page)
app.add_page(subscription_page)
app.add_page(dashboard, on_load=WorkflowState.on_load)
app.add_page(registration_page)
app.add_page(login_page)
