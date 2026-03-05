import os
import pandas as pd
from pathlib import Path
import warnings

from .mtg_sorter_reflex import ocr_engine, database, french_processor

# Ignore specific warning
warnings.filterwarnings("ignore", message=".*urllib3.*or.*chardet.*")

batch_one_dir = os.path.abspath("./mtg_sorter/images/batch_one")
batch_two_dir = os.path.abspath("./mtg_sorter/images/batch_two")
batch_three_dir = os.path.abspath("./mtg_sorter/images/batch_three")
batch_four_dir = os.path.abspath("./mtg_sorter/images/batch_four")
batch_five_dir = os.path.abspath("./mtg_sorter/images/batch_five")

scan_dir = [batch_one_dir, batch_two_dir, batch_three_dir, batch_four_dir, batch_five_dir]


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
                ocr = ocr_engine.OCREngine()
                raw_name, raw_collect = ocr.extract_name(str(filepath))
                french_lang_proc = french_processor.process_french_image(str(filepath), db=db)
                final_card = db.find_best_match(raw_name, raw_collect)
                print(type(final_card), final_card)
                if final_card:
                    french_name = french_lang_proc.get('name') if french_lang_proc else 'N/A'
                    french_set = french_lang_proc.get('set') if french_lang_proc else 'N/A'
                    print(
                        f"Matched: {filepath.name} -> "
                        f"{final_card.get('name')} ({final_card.get('set')}) {french_name} {french_set}"
                    )

                    results.append({
                        "Original_File": filepath.name,
                        "Card_Name": final_card.get("name"),
                        "Set": final_card.get("set"),
                        "Color": final_card.get("color"),
                        "Price_USD": final_card.get("price"),
                        "Rarity": final_card.get("rarity")
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
