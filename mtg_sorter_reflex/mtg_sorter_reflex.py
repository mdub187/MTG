# File: mtg_sorter_reflex/mtg_sorter_reflex.py

import reflex as rx
from mtg_sorter_reflex.pages.upload import upload_page
from mtg_sorter_reflex.pages.collection import collection_page

app = rx.App()
app.add_page(collection_page, route="/collection")
app.add_page(upload_page, route="/upload")
