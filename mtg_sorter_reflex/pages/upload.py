# File: mtg_sorter_reflex/pages/upload.py

import reflex as rx
from mtg_sorter_reflex.state import OCRState

def upload_page():
    return rx.container(
        rx.vstack(
            rx.heading("MTG Card Sorter", size="lg", margin_bottom="1em"),
            rx.box(
                rx.upload(
                    rx.vstack(
                        rx.text("Drag and drop images here or click to browse"),
                        rx.text("Supports: JPG, PNG", size="sm", color="gray"),
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
                    is_disabled=not OCRState.uploaded_files,
                ),
                rx.button(
                    "Clear",
                    on_click=OCRState.clear_results,
                    variant="outline",
                ),
                width="100%",
                justify="space-between",
                margin_top="1em",
            ),
            rx.cond(
                OCRState.error,
                rx.alert(
                    rx.alert_icon(),
                    rx.alert_title(OCRState.error),
                    status="error",
                    margin_top="1em",
                ),
            ),
            rx.divider(margin_y="1em"),
            rx.heading("Results", size="md", margin_bottom="0.5em"),
            rx.cond(
                OCRState.is_processing,
                rx.center(
                    rx.circular_progress(is_indeterminate=True),
                    padding="2em",
                ),
                rx.cond(
                    OCRState.results,
                    rx.box(
                        rx.table(
                            rx.thead(
                                rx.tr(
                                    rx.th("File"),
                                    rx.th("Card Name"),
                                    rx.th("Set"),
                                    rx.th("Color"),
                                    rx.th("Price"),
                                    rx.th("Rarity"),
                                )
                            ),
                            rx.tbody(
                                rx.foreach(
                                    OCRState.results,
                                    lambda result: rx.tr(
                                        rx.td(result["file"]),
                                        rx.td(result["name"]),
                                        rx.td(result["set"]),
                                        rx.td(result["color"]),
                                        rx.td(f"${result['price']}"),
                                        rx.td(result["rarity"]),
                                    ),
                                )
                            ),
                            width="100%",
                            size="sm",
                        ),
                        rx.button(
                            "Export to CSV",
                            on_click=lambda: rx.download(
                                filename="inventory.csv",
                                data="\n".join([
                                    "File,Card Name,Set,Color,Price,Rarity",
                                    *[
                                        f"{r['file']},{r['name']},{r['set']},{r['color']},{r['price']},{r['rarity']}"
                                        for r in OCRState.results
                                    ],
                                ]),
                                mime_type="text/csv",
                            ),
                            margin_top="1em",
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
            spacing="1em",
            width="100%",
        ),
        padding="2em",
    )
