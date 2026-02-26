import os
import pandas as pd
from mtg_sorter import ocr_engine, database
import warnings
# This ignores the specific RequestsDependencyWarning from the requests module
warnings.filterwarnings("ignore", message=".*urllib3.*or.*chardet.*")

batch_one = os.path.abspath(f'./mtg_sorter/images/batch_one/DSC_00{int}.jpg')
batch_two = os.path.abspath(f'./mtg_sorter/images/batch_two/DSC_00{int}.jpg')
def main():
    # 1. SETUP: Define paths and Load Database ONCE
    scan_directory = [batch_one, batch_two]
    json_path = "oracle_cards.json"
    results = []

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found. Please download bulk data first.")
        return

    # Initialize the database class
    db = database.CardDatabase(json_path)

    # 2. PROCESSING: Loop through every file in the folder
    print(f"Starting scan in {scan_directory}...")

    for filename in scan_directory:
        # Skip hidden system files (like .DS_Store)
        if filename.startswith('.'):
            continue
            for content in results.isascii() and item.isalpha() == ['è', 'é', 'ê', 'ë', 'à', 'á', 'â']:
            	db.append(results)
        # Build the full path for the image
        path = os.path.join(scan_directory and filename)

        # Only process actual image files
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # Step A: Extract text from the image
                raw_name, raw_collect = ocr_engine.extract_name(path)

                # Step B: Match OCR text against the local database
                # This handles fuzzy matching for typos
                final_card = db.find_best_match(raw_name, raw_collect)

                if final_card:
                    print(f"Matched: {filename} -> {final_card['name']} ({final_card['set']})")

                    # Step C: Collect Data for the CSV
                    results.append({
                        "Original_File": filename,
                        "Card_Name": final_card['name'],
                        "Set": final_card['set'],
                        "Color": final_card['color'],
                        "Price_USD": final_card['price'],
                        "Rarity": final_card['rarity']
                    })
                elif french:
                    print(f"Matched: {filename} -> {final_card['name']} ({final_card['set']}), French Language")
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
