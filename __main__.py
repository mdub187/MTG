import os
import pandas as pd
from pathlib import Path
import warnings

from mtg_sorter import ocr_engine, database, french_processor

# Ignore specific warning
warnings.filterwarnings("ignore", message=".*urllib3.*or.*chardet.*")

batch_one_dir = os.path.abspath("./mtg_sorter/images/batch_one")
batch_two_dir = os.path.abspath("./mtg_sorter/images/batch_two")
batch_three_dir = os.path.abspath("./mtg_sorter/images/batch_three")
batch_four_dir = os.path.abspath("./mtg_sorter/images/batch_four")

scan_dir = [batch_one_dir, batch_two_dir, batch_three_dir, batch_four_dir]


def main():
    # 1. SETUP
    json_path = "oracle_cards.json"
    results = []

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found. Please download bulk data first.")
        return

    db = database.CardDatabase(json_path)

    print(f"Starting scan in {scan_dir}...")

    # 2. PROCESSING
    for directory in scan_dir:
        dir_path = Path(directory)

        if not dir_path.exists():
            print(f"Directory missing: {directory}")
            continue

        for filepath in dir_path.iterdir():

            if not filepath.is_file():
                continue

            if filepath.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
                continue

            print(f"Processing: {filepath.name}")

            try:
                raw_name, raw_collect = ocr_engine.extract_name(str(filepath))
                french_lang_proc = french_processor.process_french_batch(str(filepath))
                final_card = db.find_best_match(raw_name, raw_collect)
                print(type(final_card), final_card)
                if final_card:
                    print(
                        f"Matched: {filepath.name} -> "
                        f"{final_card['name']} ({final_card['set']}) {(french_lang_proc['name'])} {(french_lang_proc['set'])}"
                    )

                    results.append({
                        "Original_File": filepath.name,
                        "Card_Name": final_card["name"],
                        "Set": final_card["set"],
                        "Color": final_card["color"],
                        "Price_USD": final_card["price"],
                        "Rarity": final_card["rarity"]
                    })

                else:
                    print(
                        f"Could not identify: {filepath.name} "
                        f"(OCR read: '{raw_name}')"
                    )

            except Exception as e:
                print(f"Error processing {filepath.name}: {e}")

    # 3. OUTPUT
    if results:
        df = pd.DataFrame(results)
        df.to_csv("mtg_sorter/card_scans/master_inventory.csv", index=False)

        print("\n" + "=" * 30)
        print(f"SUCCESS! {len(results)} cards processed.")
        print("Final report saved to: master_inventory.csv")
        print("=" * 30)

    else:
        print("No cards were successfully matched.")


if __name__ == "__main__":
    main()
