import reflex as rx
from . import navbar

def template() -> rx.Component:
    return rx.box(
        navbar,
    )
