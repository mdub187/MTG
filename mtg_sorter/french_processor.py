import os
import json
import pandas as pd
from .ocr_engine import extract_name
from .database import CardDatabase

def process_french_batch(scan_dir=["./images/batch_one/", "./images/batch_two/", "./images/batch_three/", "./images/batch_four/"], json_path="./oracle_cards.json"):
    """
    Independent runner for French language card sorting.
    """
    if not os.path.exists(json_path):
        print(f"Error: {json_path} (Default Cards) is required for French support.")
        return

    # Load Database with French Indexing
    db = CardDatabase(json_path)
    results = []

    print(f"Scanning French cards in {scan_dir}...")
    for directory in scan_dir:
        for filename in os.listdir(directory):
            if filename.startswith('.') or not filename.lower().endswith(('.jpg', '.png')):
                continue

            path = os.path.join(directory, filename)

            # Use OCR with French language support
            raw_name, raw_collect = extract_name(path)

            # Check if the OCR result contains French diacritics
            has_french_diacritics = any(char in raw_name for char in ['è', 'é', 'ê', 'ë', 'à', 'á', 'â', 'î', 'ï', 'ô', 'û', 'ù', 'ü', 'ç'])

            if has_french_diacritics:
                # Database lookup (handles 'printed_name' for French)
                match = db.find_best_match(raw_name, raw_collect)
                if match and match.get('lang') == 'fr':
                    print(f"French Match: {filename} -> {match['printed_name']} ({match['set']})")
                    results.append({
                        "File": filename,
                        "French_Name": match['printed_name'],
                        "English_Name": match['name'],
                        "Set": match['set'],
                        "Price": match.get('price', 'N/A')
                    })
                else:
                    print(f"No French match found for: {filename}")
            else:
                print(f"Skipping non-French card: {filename}")

    # Output to a specific French inventory file
    if results:
        df = pd.DataFrame(results)
        df.to_csv("./french_inventory.csv", index=False)
        print(f"Success! {len(results)} French cards documented in french_inventory.csv")

if __name__ == "__main__":
	print("french_processor.py")
    # process_french_batch()
