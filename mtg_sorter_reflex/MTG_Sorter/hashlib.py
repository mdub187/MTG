import imagehash
from PIL import Image
import json
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.append(project_root)

# Import after ensuring the path is set
from mtg_sorter_reflex.MTG_Sorter.master_sort import db_path
image_path = db_path


def generate_fingerprint(image_path):
    """Creates a 64-bit perceptual hash for a card image."""
    return str(imagehash.phash(Image.open(image_path)))


def compare_hashes(hash1, hash2):
    """Returns the Hamming Distance; lower is a closer match."""
    return imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)
