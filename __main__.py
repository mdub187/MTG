import os
import pandas as pd
from mtg_sorter import ocr_engine, database, master_sort
import warnings
from pathlib import Path
# This ignores the specific RequestsDependencyWarning from the requests module
warnings.filterwarnings("ignore", message=".*urllib3.*or.*chardet.*")

batch_one_dir = os.path.abspath("./mtg_sorter/images/batch_one")
batch_two_dir = os.path.abspath("./mtg_sorter/images/batch_two")
batch_three_dir = os.path.abspath("./mtg_sorter/images/batch_three")
batch_four_dir = os.path.abspath("./mtg_sorter/images/batch_four")

scan_directory = [batch_one_dir, batch_two_dir, batch_three_dir, batch_four_dir]
def main():
    # 1. SETUP: Define paths and Load Database ONCE
    json_path = "oracle_cards.json"
    results = []

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found. Please download bulk data first.")
        return

    # Initialize the database class
    db = database.CardDatabase(json_path)

    # 2. PROCESSING: Loop through every file in the folder
    print(f"Starting scan in {scan_directory}...")

    for directory in scan_directory:
        for filename in os.listdir(directory):

            if filename.startswith('.'):
                continue

            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                path = os.path.join(directory, filename)

                try:
                    raw_name, raw_collect = ocr_engine.extract_name(path)
                    final_card = db.find_best_match(raw_name, raw_collect)

                    if final_card:
                        print(f"Matched: {filename} -> {final_card['name']} ({final_card['set']})")

                        results.append({
                            "Original_File": filename,
                            "Card_Name": final_card['name'],
                            "Set": final_card['set'],
                            "Color": final_card['color'],
                            "Price_USD": final_card['price'],
                            "Rarity": final_card['rarity']
                        })
                    else:
                        print(f"Could not identify: {filename} (OCR read: '{raw_name}')")

                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    # 3. OUTPUT: Save all results to a single CSV
    if results:
        # from .mtg_sorter import master_sort
        master = Path("./card_scans/")
        base = master / "scans.csv"
        parent = base.parent
        csv = parent.name
        print(csv)
        df = pd.DataFrame(results)
        df.to_csv(master, index=False)
        print("\n" + "="*30)
        print(f"SUCCESS! {len(results)} cards processed.")
        print("Final report saved to: master_inventory.csv")
        print("="*30)
    else:
        print("No cards were successfully matched.")

if __name__ == "__main__":
    main()
