import imagehash
from PIL import Image
import scrython
import requests
from io import BytesIO
from .master_sort import image_folder


image_path = image_folder
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
    try:
        printings = scrython.cards.Search(q=f'!"{card_name}" unique:prints')

        # Convert to list if it's a Search object
        if hasattr(printings, 'data') and callable(getattr(printings, 'data')):
            printing_list = printings.data()
        elif isinstance(printings, list):
            printing_list = printings
        else:
            import sys
            print(f"Unexpected Scryfall response type: {type(printings)}", file=sys.stderr)
            return None, 64
    except Exception as e:
        import sys
        print(f"Scryfall API error: {e}", file=sys.stderr)
        return None, 64

    if not printing_list:
        import sys
        print(f"No printings found for {card_name}", file=sys.stderr)
        return None, 64

    best_match_set = None
    lowest_distance = 64  # Max distance for a 64-bit hash

    import sys
    print(f"Comparing {card_name} against {len(printing_list)} versions...", file=sys.stderr)

    for version in printing_list:
        try:
            # Download the official art thumbnail for comparison
            img_url = version["image_uris"]["normal"]
            response = requests.get(img_url)
            official_img = Image.open(BytesIO(response.content))

            # Hash the official image
            official_hash = imagehash.phash(official_img)

            # Calculate 'distance' (0 is an identical match)
            distance = scan_hash - official_hash

            if distance < lowest_distance:
                lowest_distance = distance
                best_match_set = version["set_name"]

        except KeyError:
            continue  # Skip versions without images (tokens/special extras)

    return best_match_set, lowest_distance


# Example Usage:
# set_detected, confidence = find_exact_printing('card_scans/bolt.jpg', 'Lightning Bolt')
# print(f"Detected Set: {set_detected} (Distance: {confidence})")
