# File: mtg_sorter/__main__.py

from . import extract_name, CardDatabase
from .master_sort import process_inventory
import os
import sys

# Add the project root to the system path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    print(f"Package 'mtg_sorter' initialized as: {__name__}")
    image_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "images"))
    print(f"Starting scan in {image_root}...")
    process_inventory(image_root)
