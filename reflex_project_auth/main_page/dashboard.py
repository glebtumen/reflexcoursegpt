import reflex as rx


@rx.page(route="/dashboard")
def dashboard() -> rx.Component:
    # Header: Displays the title and subscription status.
    header = rx.hstack(
        rx.heading("КурсачГПТ", class_name="text-3xl font-bold"),
        rx.text("Доступ до: дата", class_name="text-lg"),
        justify="between",
        align_items="center",
        width="100%",
        padding="1",
    )

    # Left panel: Chat modes selection.
    chat_modes = rx.vstack(
        rx.button("Курсовая", width="100%"),
        rx.button("Курсовая по содержанию", width="100%"),
        rx.button("Свободный режим", width="100%"),
        spacing="1",
        padding="1",
    )

    # Center panel: Input field and chat display.
    chat_input = rx.input(placeholder="Введите сообщение...", width="100%", padding="1")
    chat_box = rx.box(
        rx.text("Chat messages will appear here..."),
        width="100%",
        border="1px solid #ccc",
        overflow_y="auto",
        padding="1",
    )
    center_panel = rx.vstack(chat_input, chat_box, spacing="1", width="100%")

    # Right panel: Chat settings.
    chat_settings = rx.vstack(
        rx.text("Настройки чата", class_name="text-xl font-bold"),
        rx.hstack(
            rx.text("Temperature:"),
            rx.input(type="range", min="0", max="1", step="0.01", default_value="0.5"),
            spacing="1",
        ),
        rx.hstack(
            rx.text("Creativeness:"),
            rx.input(type="range", min="0", max="1", step="0.01", default_value="0.5"),
            spacing="1",
        ),
        rx.hstack(
            rx.text("Text Size:"),
            rx.input(type="number", default_value="14", min="10", max="30"),
            spacing="1",
        ),
        spacing="1",
        padding="1",
    )

    # Main chat area: Arrange left, center, and right panels.
    main_chat_area = rx.hstack(
        chat_modes, center_panel, chat_settings, spacing="2", padding="1"
    )

    return rx.vstack(header, main_chat_area, spacing="2", padding="2")
