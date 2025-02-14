import reflex as rx


def main_content() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.heading(
                "Welcome to Our Landing Page",
                class_name="text-4xl font-bold text-center text-blue-500",
            )
        ),
        rx.center(
            rx.text(
                "Your one-stop solution for amazing services.",
                class_name="text-xl text-gray-700 text-center",
            )
        ),
        rx.center(
            rx.image(
                src="https://via.placeholder.com/600x300",
                alt="Main Photo",
                class_name="rounded-lg shadow-lg",
            )
        ),
        rx.center(
            rx.text(
                "Discover our features and offerings.",
                class_name="text-lg text-gray-700 text-center mt-4",
            )
        ),
        rx.hstack(
            rx.image(
                src="https://via.placeholder.com/300",
                alt="Photo 1",
                class_name="rounded-lg shadow-md",
            ),
            rx.image(
                src="https://via.placeholder.com/300",
                alt="Photo 2",
                class_name="rounded-lg shadow-md",
            ),
            justify="center",
            spacing="4",
            class_name="mt-4",
        ),
        rx.center(
            rx.heading(
                "Customer Reviews",
                class_name="text-3xl font-semibold text-gray-800 mt-8",
            )
        ),
        rx.center(
            rx.text(
                "Our customers love us!", class_name="text-lg text-gray-700 text-center"
            )
        ),
        rx.center(
            rx.heading(
                "Pricing", class_name="text-3xl font-semibold text-gray-800 mt-8"
            )
        ),
        rx.center(
            rx.text(
                "Choose a pricing plan that suits you.",
                class_name="text-lg text-gray-700 text-center",
            )
        ),
        rx.center(
            rx.heading(
                "Get Started Today",
                class_name="text-3xl font-semibold text-gray-800 mt-8",
            )
        ),
        rx.center(
            rx.button(
                "Join Us",
                variant="solid",
                color_scheme="blue",
                class_name="px-6 py-3 text-lg font-medium rounded",
            )
        ),
        rx.center(
            rx.heading("FAQ", class_name="text-3xl font-semibold text-gray-800 mt-8")
        ),
        rx.center(
            rx.text(
                "Frequently asked questions will appear here.",
                class_name="text-lg text-gray-700 text-center",
            )
        ),
        spacing="8",
        padding="8",
        class_name="bg-white",
        align="center",
    )
