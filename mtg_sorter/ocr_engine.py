import os
import cv2
import pytesseract
import pandas as pd


def extract_name(image_path):
    """
    OCR function to extract card name and collector info.
    Supports English + French in one pass.
    """
    img = cv2.imread(image_path)
    if img is None:
        return None, None

    h, w, _ = img.shape

    # Name ROI (top-left)
    name_roi = img[int(h * 0.04):int(h * 0.11), int(w * 0.05):int(w * 0.65)]

    # Collector ROI (bottom-left)
    collect_roi = img[int(h * 0.91):int(h * 0.97), int(w * 0.05):int(w * 0.35)]

    def clean_roi(roi):
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        return thresh

    name_text = pytesseract.image_to_string(
        clean_roi(name_roi),
        lang="eng+fra",
        config="--psm 7"
    ).strip()

    collect_text = pytesseract.image_to_string(
        clean_roi(collect_roi),
        lang="eng+fra",
        config="--psm 7"
    ).strip()

    return name_text, collect_text


def process_batch(
    scan_dirs=None,
    json_path="./oracle_cards.json"
):
    """
    Unified runner for mixed-language card sorting.
    """
    if scan_dirs is None:
        scan_dirs = [
            "./images/batch_one/",
            "./images/batch_two/",
            "./images/batch_three/"
        ]

    if not os.path.exists(json_path):
        print(f"Error: {json_path} is required.")
        return

    db = CardDatabase(json_path)
    results = []

    print(f"Scanning cards in {scan_dirs}...")

    for scan_dir in scan_dirs:
        for filename in os.listdir(scan_dir):

            if filename.startswith('.') or not filename.lower().endswith(('.jpg', '.png')):
                continue

            path = os.path.join(scan_dir, filename)

            raw_name, raw_collect = extract_name(path)
            if not raw_name:
                print(f"Could not identify: {filename}")
                continue

            match = db.find_best_match(raw_name, raw_collect)

            if match:
                print(f"Match: {filename} -> {match['name']} ({match['set']})")

                results.append({
                    "File": filename,
                    "Printed_Name": match.get('printed_name'),
                    "English_Name": match.get('name'),
                    "Set": match.get('set'),
                    "Colors": match.get('color'),
                    "Price_USD": match.get('price'),
                    "Rarity": match.get('rarity'),
                    "Language": match.get('lang')
                })
            else:
                print(f"No match found: {filename}")

    if results:
        df = pd.DataFrame(results)
        df.to_csv("./inventory.csv", index=False)
        print(f"Success! {len(results)} cards documented.")


if __name__ == "__main__":
    process_batch()
