import reflex as rx


@rx.page(route="/help")
def help_page():
    return rx.box(
        rx.vstack(
            rx.markdown(
                r"""# Markdown Component

The rx.markdown component can be used to render markdown text. It is based on GitHub Flavored Markdown.

Hello World!
Hello World!
Hello World!
Support us on Github.

Use `reflex deploy` to deploy your app with a single command.

Example:
rx.vstack(
    rx.markdown("# Hello World!"),
    rx.markdown("## Hello World!"),
    rx.markdown("### Hello World!"),
    rx.markdown(
        "Use `reflex deploy` to deploy your app with **a single command**."
    ),
)
"""
            ),
            align="center",
        )
    )
