import reflex as rx
from mtg_sorter_reflex.components.navbar import navbar


route = "/login"


def login_page():
    return rx.container(
        navbar(),
        rx.form(
            rx.input(name="username", placeholder="Username"),
            rx.input(name="password", placeholder="Password", type="password"),
            rx.button("Login", type="submit"),
        ),

    )