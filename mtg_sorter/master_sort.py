import os
import json
import pandas as pd
from difflib import get_close_matches
from pathlib import Path
from .french_processor import process_french_batch
path = Path('./oracle_cards.json')
# 1. Load the local database
with open(path, 'r', encoding='utf-8') as f:
    path = json.load(f)

# Create a searchable dictionary: { "Card Name": {data} }
mtg_db = {card['name'].lower(): card for card in path}
valid_names = list(mtg_db.keys())

def lookup_card_locally(ocr_name):
    name_low = ocr_name.lower()

    # Direct match or Fuzzy match for OCR errors
    match = get_close_matches(name_low, valid_names, n=1, cutoff=0.8)
    if match:
        card = mtg_db[match[0]]
        return {
            "Name": card['name'],
            "Colors": "".join(card.get('color_identity', [])),
            "Set": card.get('set_name', 'Unknown'),
            "USD_Price": card.get('prices', {}).get('usd', '0.00'),
            "Rarity": card.get('rarity', 'unknown')
        }
    return None
image_folder=['/MTG/mtg_sorter/images/batch_one/', '/MTG/mtg_sorter/images/batch_two/', "/MTG/mtg_sorter/images/batch_three/", "/MTG/mtg_sorter/images/batch_four/", "/MTG/mtg_sorter/images/batch_five/"]
def process_inventory(image_folder):
    results = []
    for folder in image_folder:
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.jpg', '.png')):
                ocr_name = os.path.splitext(filename)[0]
                data = lookup_card_locally(ocr_name)
                if data:
                    results.append(data)
                    print(f"Matched: {ocr_name} -> {data['Name']}")

    # Save non-French cards to CSV
    df = pd.DataFrame(results)
    df.to_csv('./card_inventory.csv', index=False)
    print(f"Success! {len(results)} non-French cards documented in card_inventory.csv")

    # Process French cards separately
    process_french_batch(scan_dir=image_folder, json_path="./oracle_cards.json")
