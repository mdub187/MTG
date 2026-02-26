import imagehash
from PIL import Image
import scrython
import requests
from io import BytesIO

def get_image_hash(image_path):
    """Generates a 64-bit perceptual hash of the image."""
    return imagehash.phash(Image.open(image_path))

def find_exact_printing(scan_path, card_name):
    """
    Compares a scan against every printing of a specific card name
    to find the correct set/edition.
    """
    # 1. Get the hash of your physical scan
    scan_hash = get_image_hash(scan_path)

    # 2. Fetch all printings of this card from Scryfall
    # Note: Using the API here for specific version images
    printings = scrython.cards.Search(q=f'!"{card_name}" unique:prints')

    best_match_set = None
    lowest_distance = 64 # Max distance for a 64-bit hash

    print(f"Comparing {card_name} against {len(printings.data())} versions...")

    for version in printings.data():
        try:
            # Download the official art thumbnail for comparison
            img_url = version['image_uris']['normal']
            response = requests.get(img_url)
            official_img = Image.open(BytesIO(response.content))

            # Hash the official image
            official_hash = imagehash.phash(official_img)

            # Calculate 'distance' (0 is an identical match)
            distance = scan_hash - official_hash

            if distance < lowest_distance:
                lowest_distance = distance
                best_match_set = version['set_name']

        except KeyError:
            continue # Skip versions without images (tokens/special extras)

    return best_match_set, lowest_distance

# Example Usage:
# set_detected, confidence = find_exact_printing('card_scans/bolt.jpg', 'Lightning Bolt')
# print(f"Detected Set: {set_detected} (Distance: {confidence})")
