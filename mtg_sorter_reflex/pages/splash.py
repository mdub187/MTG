import reflex as rx
from ..cond.login_buton_display import login_button, CondState
from mtg_sorter_reflex.components.navbar import navbar
route = "/home"


def index():
    return rx.container(
        navbar(),
        rx.heading("Home Page", size="3"),
            # rx.heading("Collection", size="2"),
        rx.text("welcome home"),
        rx.container(
            rx.button(rx.link("Upload", href="/upload")),
            rx.button(rx.link("Collection", href="/collection")),
            rx.button(login_button())
        )
    )
index()
