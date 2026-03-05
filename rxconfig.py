import reflex as rx

config = rx.Config(
    app_name="mtg_sorter_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
