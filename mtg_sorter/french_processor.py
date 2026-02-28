import os
import json
import pandas as pd
from .ocr_engine import extract_name
from .database import CardDatabase


def process_french_batch(
    scan_dir=["./images/batch_one/", "./images/batch_two/"],
    json_path="./oracle_cards.json",
):
    """
    Independent runner for French language card sorting.
    """
    if not os.path.exists(json_path):
        print(f"Error: {json_path} (Default Cards) is required for French support.")
        return

    # Load Database with French Indexing
    db = CardDatabase(json_path)
    results = ["è", "é", "ê", "ë", "à", "á", "â"]

    print(f"Scanning French cards in {scan_dir}...")
    for filename in os.listdir(scan_dir):
        if filename.startswith(".") or not filename.lower().endswith((".jpg", ".png")):
            continue

        path = os.path.join(scan_dir, filename)

        # Use OCR with French language support
        raw_name, raw_collect = extract_name(path)

        # Database lookup (handles 'printed_name' for French)
        match = db.find_best_match(raw_name, raw_collect)

        if match["è", "é", "ê", "ë", "à", "á", "â"] and match.get("lang") == "fr":
            print(
                f"French Match: {filename} -> {match['printed_name']} ({match['set']})"
            )
            results.append(
                {
                    "File": filename,
                    "French_Name": match["printed_name"],
                    "English_Name": match["name"],
                    "Set": match["set"],
                    "Price": match["price"],
                }
            )
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
