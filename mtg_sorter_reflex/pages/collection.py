import reflex as rx
from mtg_sorter_reflex.components.navbar import navbar


route = "/collection"


def collection_page():
    return rx.container(
        navbar(),
        rx.heading("Collection", size="2"),

    )
