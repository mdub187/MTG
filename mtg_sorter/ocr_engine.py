import cv2
import pytesseract


image_path = "./images/"
def extract_name(image_path):
    """
    Primary OCR function to get the card name and collector info.
    """
    img = cv2.imread(image_path)
    if img is None:
        return None, None

    h, w, _ = img.shape

    # 1. ROI for Name Bar (Top Left)
    # Adjust percentages if your scans have large borders
    name_roi = img[int(h*0.04):int(h*0.11), int(w*0.05):int(w*0.65)]

    # 2. ROI for Collector Info (Bottom Left)
    # This helps differentiate between sets (e.g., "123/280 M21 EN")
    collect_roi = img[int(h*0.91):int(h*0.97), int(w*0.05):int(w*0.35)]

    # Pre-processing (Grayscale + Threshold)
    def clean_roi(roi):
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # Thresholding helps OCR see text against dark/colored backgrounds
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        return thresh

    name_text = pytesseract.image_to_string(clean_roi(name_roi), lang="eng+fra", config="--psm 7").strip()
    collect_text = pytesseract.image_to_string(clean_roi(collect_roi), lang="en+fra", config="--psm 7").strip()

    return name_text, collect_text
