import reflex as rx


class AppConfig(rx.Config):
    """Custom configuration for the Reflex application."""

    pass


config = AppConfig(
    app_name="reflex_project_auth",
    telemetry_enabled=False,
    env=rx.Env.DEV,
    tailwind={
        "theme": {
            "extend": {"fontFamily": {"manrope": ["Manrope"], "roboto": ["Roboto"]}},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
