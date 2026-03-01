import imagehash
from PIL import Image
import json
from .master_sort import image_folder
image_path = image_folder


def generate_fingerprint(image_path):
    """Creates a 64-bit perceptual hash for a card image."""
    return str(imagehash.phash(Image.open(image_path)))


def compare_hashes(hash1, hash2):
    """Returns the Hamming Distance; lower is a closer match."""
    return imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)
