import os
import json
import pandas as pd
from .ocr_engine import OCREngine
from .database import CardDatabase
from .ocr_engine import OCREngine

def process_french_image(image_path, db=None):
    """
    Process a single French card image.
    
    Args:
        image_path: Path to the image file.
        db: Pre-loaded CardDatabase instance to avoid reloading.
    """
    if db is None:
        json_path="./oracle_cards.json"
        if not os.path.exists(json_path):
            print(f"Error: {json_path} (Default Cards) is required for French support.")
            return
        db = CardDatabase(json_path)

    # Use OCR with French language support
    ocr = OCREngine()
    raw_name, raw_collect = ocr.extract_name(image_path)

    # Database lookup (handles 'printed_name' for French)
    match = db.find_best_match(raw_name, raw_collect)

    if match and isinstance(match, dict) and any(char in match.get('printed_name', '') for char in ['è', 'é', 'ê', 'ë', 'à', 'á', 'â']) and match.get('lang') == 'fr':
        print(f"French Match: {os.path.basename(image_path)} -> {match['printed_name']} ({match['set']}) ({match['color']})")
        return match
    return None

def process_french_batch(scan_dir=["./images/batch_one/", "./images/batch_two/", "./images/batch_three/", "./images/batch_four/"], db=None):
    """
    Independent runner for French language card sorting.
    
    Args:
        scan_dir: List of directories to scan for French card images.
        db: Pre-loaded CardDatabase instance to avoid reloading.
    """
    if db is None:
        json_path="./oracle_cards.json"
        if not os.path.exists(json_path):
            print(f"Error: {json_path} (Default Cards) is required for French support.")
            return
        db = CardDatabase(json_path)
    results = []

    print(f"Scanning French cards in {scan_dir}...")
    for directory in scan_dir:
        if not os.path.isdir(directory):
            continue

        for filename in os.listdir(directory):
            if filename.startswith(".") or not filename.lower().endswith((".jpg", ".png")):
                continue

            path = os.path.join(directory, filename)

            # Use OCR with French language support
            ocr = OCREngine()
            raw_name, raw_collect = ocr.extract_name(path)

            # Database lookup (handles 'printed_name' for French)
            match = db.find_best_match(raw_name, raw_collect)

            if match and isinstance(match, dict) and any(char in match.get('printed_name', '') for char in ['è', 'é', 'ê', 'ë', 'à', 'á', 'â']) and match.get('lang') == 'fr':
                print(f"French Match: {filename} -> {match['printed_name']} ({match['set']}) ({match['color']})")
                results.append({
                    "File": filename,
                    "French_Name": match['printed_name'],
                    "English_Name": match['name'],
                    "Set": match['set'],
                    "Colors": match['color'],
                    "Price_USD": match['price'],
                    "Rarity": match['rarity']
                })
            else:
                print(f"Skipping non-French or unknown card: {filename}")

    # Output to a specific French inventory file
    if results:
        df = pd.DataFrame(results)
        df.to_csv("./card_scans/french_inventory.csv", index=False)
        print(
            f"Success! {len(results)} French cards documented in french_inventory.csv"
        )


if __name__ == "__main__":
    process_french_batch()
