import os
import pandas as pd
from mtg_sorter import ocr_engine, database
import warnings

# This ignores the specific RequestsDependencyWarning from the requests module
warnings.filterwarnings("ignore", message=".*urllib3.*or.*chardet.*")
from mtg_sorter.master_sort import process_inventory


Path = os.path.abspath("./mtg_sorter/images/*")
scan_directory = process_inventory
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
    image_root = "./mtg_sorter/images/"

    for directory in image_root:
        for filename in Path:

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
        df = pd.DataFrame(results)
        df.to_csv("master_inventory.csv", index=False)
        print("\n" + "="*30)
        print(f"SUCCESS! {len(results)} cards processed.")
        print("Final report saved to: master_inventory.csv")
        print("="*30)
    else:
        print("No cards were successfully matched.")

if __name__ == "__main__":
    main()
