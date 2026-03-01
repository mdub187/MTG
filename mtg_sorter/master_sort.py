
import os
import json
import pandas as pd
from difflib import get_close_matches
from pathlib import Path
from . import ocr_engine

# Load the local database
db_path = Path("/Users/mdub/Documents/MTG_Sorter/oracle_cards.json")
with open(db_path, "r", encoding="utf-8") as f:
    bulk_data = json.load(f)

# Create a searchable dictionary: { "Card Name": {data} }
mtg_db = {card["name"].lower(): card for card in bulk_data}
valid_names = list(mtg_db.keys())


# Update lookup_card_locally in master_sort.py
def lookup_card_locally(ocr_name):
    if not ocr_name:
        return None

    # Normalize the OCR output
    normalized_name = normalize_ocr_text(ocr_name)
    print(f"Normalized name: '{normalized_name}'")

    # Try direct match
    if normalized_name.lower() in mtg_db:
        card = mtg_db[normalized_name.lower()]
        return {
            "Name": card["name"],
            "Colors": "".join(card.get("color_identity", [])),
            "Set": card.get("set_name", "Unknown"),
            "USD_Price": card.get("prices", {}).get("usd", "0.00"),
            "Rarity": card.get("rarity", "unknown"),
        }

    # Try matching against original and normalized versions
    name_versions = [
        ocr_name.lower(),
        normalized_name.lower(),
        re.sub(r'[^a-zA-Z0-9 ]', '', ocr_name).lower(),
        re.sub(r'[^a-zA-Z0-9 ]', '', normalized_name).lower(),
    ]

    for name_version in name_versions:
        match = get_close_matches(name_version, valid_names, n=1, cutoff=0.7)
        if match:
            card = mtg_db[match[0]]
            return {
                "Name": card["name"],
                "Colors": "".join(card.get("color_identity", [])),
                "Set": card.get("set_name", "Unknown"),
                "USD_Price": card.get("prices", {}).get("usd", "0.00"),
                "Rarity": card.get("rarity", "unknown"),
            }

    return None

def find_images(root_dir):
    if not os.path.exists(root_dir):
        raise FileNotFoundError(f"Image directory not found at {root_dir}")

    image_extensions = (".jpg", ".jpeg", ".png", ".JPG", ".PNG")
    image_paths = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(image_extensions):
                image_paths.append(os.path.join(dirpath, filename))

    if not image_paths:
        print(f"No images found in {root_dir} with extensions {image_extensions}")

    return image_paths

def process_inventory(image_root):
    results = []
    image_paths = find_images(image_root)

    if not image_paths:
        print("No images to process. Exiting...")
        return

    print(f"Found {len(image_paths)} images to process")

    for image_path in image_paths:
        print(f"\nProcessing image: {image_path}")
        card_name, collect_name = ocr_engine.extract_name(image_path)

        print(f"  - Extracted name: '{card_name}'")
        print(f"  - Extracted collect: '{collect_name}'")

        data = lookup_card_locally(card_name) or lookup_card_locally(collect_name)
        if data:
            results.append(data)
            print(f"  - Matched: {os.path.basename(image_path)} -> {data['Name']}")
        else:
            print("  - No match found in the database")

    # Save to CSV
    if results:
        output_path = os.path.join(os.path.dirname(__file__), "..", "card_scans", "master_inventory.csv")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pd.DataFrame(results).to_csv(output_path, index=False)
        print(f"\nResults saved to {output_path}")
        print(f"Successfully matched {len(results)}/{len(image_paths)} images")
    else:
        print("\nNo results to save. Check OCR output and database matches.")
