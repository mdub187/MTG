import os
import json
import pandas as pd
from difflib import get_close_matches

# 1. Load the local database
with open('../oracle_cards.json', 'r', encoding='utf-8') as f:
    bulk_data = json.load(f)

# Create a searchable dictionary: { "Card Name": {data} }
mtg_db = {card['name'].lower(): card for card in bulk_data}
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
image_folder=['/MTG_Sorter/mtg_sorter/images/batch_one/', '/MTG_Sorter/mtg_sorter/images/batch_two/' ]
def process_inventory(image_folder):
    results = []
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.JPG', '.png')):
            ocr_name = os.path.splitext(filename)[0]
            data = lookup_card_locally(ocr_name)
            if data:
                results.append(data)
                print(f"Matched: {ocr_name} -> {data['Name']}")

    # Save to CSV
    pd.DataFrame(results).to_csv("master_inventory.csv", index=False)

process_inventory('./card_scans/')
