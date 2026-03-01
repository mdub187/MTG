# mtg_sorter/__init__.py
from .ocr_engine import extract_name
from .database import CardDatabase



if __name__ == "__main__":
    print(f"Package 'mtg_sorter' initialized as: {__name__}")
    # Your main sorting logic goes here...
    print(extract_name, CardDatabase)
