import reflex as rx


def background_v3():
    return rx.center(
        rx.html(
            "Твой ИИ для <br> курсовых работ",
            class_name=" text-6xl md:text-8xl lg:text-8xl tracking-[-0.055em] text-center text-black font-extrabold font-manrope",
        ),
        background_size="100px 100px",
        background_image="linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)",
        mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0.3))",
        width="100%",
        height="55vh",
    )
