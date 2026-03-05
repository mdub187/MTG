
import reflex as rx


def login_page():
    return rx.container(
        rx.form(
            rx.input(name="username", placeholder="Username"),
            rx.input(name="password", placeholder="Password", type="password"),
            rx.button("Login", type="submit"),
        ),

    )
