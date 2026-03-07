# File: mtg_sorter_reflex/pages/upload.py

import reflex as rx
from mtg_sorter_reflex.state import OCRState
from mtg_sorter_reflex.components import navbar


route = "/upload"


def upload_page() -> rx.Component:
    return rx.container(
        rx.box(
            navbar.navbar(),
        ),
        rx.vstack(
            rx.heading("MTG Card Sorter", size="5", margin_bottom=3),
            rx.box(
            ),
            rx.box(
                rx.upload(
                    rx.vstack(
                        rx.text("Drag and drop images here or click to browse"),
                        rx.text("Supports: JPG, PNG", size="6", color="gray"),
                    ),
                    border="1px dashed gray",
                    padding="2em",
                    border_radius="md",
                    accept={
                        "image/jpeg": [".jpg", ".jpeg"],
                        "image/png": [".png"],
                    },
                    multiple=True,
                    max_files=20,
                    on_drop=OCRState.handle_upload,
                    width="100%",
                ),
                width="100%",
            ),
            rx.hstack(
                rx.button(
                    "Process Images",
                    on_click=OCRState.process_images,
                    is_loading=OCRState.is_processing,
                    is_disabled=rx.cond(OCRState.uploaded_files, False, True),
                ),
                rx.button(
                    "Clear",
                    on_click=OCRState.clear_results,
                    variant="outline",
                ),
                width="100%",
                margin_top=3,
            ),
            rx.divider(margin_y="1em"),
            rx.heading("Results", size="5", margin_bottom=3),
            rx.cond(
                OCRState.is_processing,
                rx.center(
                    rx.spinner(),
                    padding="2em",
                ),
                rx.cond(
                    OCRState.results,
                    rx.vstack(
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("File"),
                                    rx.table.column_header_cell("Card Name"),
                                    rx.table.column_header_cell("Set"),
                                    rx.table.column_header_cell("Color"),
                                    rx.table.column_header_cell("Price"),
                                    rx.table.column_header_cell("Rarity"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    OCRState.results,
                                    lambda result: rx.table.row(
                                        rx.table.cell(result["file"]),
                                        rx.table.cell(result["name"]),
                                        rx.table.cell(result["set"]),
                                        rx.table.cell(result["color"]),
                                        rx.table.cell(f"${result['price']}"),
                                        rx.table.cell(result["rarity"]),
                                    ),
                                ),
                            ),
                        ),
                        rx.button(
                            "Export to CSV",
                            on_click=OCRState.export_to_csv,
                            margin_top=3,
                            width="100%",
                        ),
                        width="100%",
                    ),
                    rx.text(
                        "No results yet. Upload and process images to see results.",
                        color="gray.500",
                        text_align="center",
                        padding="2em",
                    ),
                ),
            ),
            spacing="3",
            width="100%",
            padding="2em",
        )
    )
