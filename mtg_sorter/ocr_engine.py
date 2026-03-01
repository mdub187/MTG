
import cv2
import pytesseract
import numpy as np
import sys
import re

Path = "./images/"

def enhance_card_image(img):
    """Enhances the card image for better OCR accuracy"""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # Remove small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    return cleaned

def extract_name(Path, lang="eng"):
    img = cv2.imread(Path)
    if img is None:
        print(f"Error: Could not read image at {Path}", file=sys.stderr)
        return None, None

    h, w = img.shape[:2]
    print(f"Image dimensions: {w}x{h}")

    # Define ROIs with tighter bounds
    name_roi = img[int(h * 0.1):int(h * 0.2), int(w * 0.1):int(w * 0.9)]
    collect_roi = img[int(h * 0.8):int(h * 0.85), int(w * 0.1):int(w * 0.5)]

    # Process ROIs
    name_clean = enhance_card_image(name_roi)
    collect_clean = enhance_card_image(collect_roi)

    # Configure Tesseract to recognize only card-relevant characters
    custom_config = r'--psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-:.,;()[]{}\'""?!&|_-"'

    # Extract text
    name_text = pytesseract.image_to_string(name_clean, lang=lang, config=custom_config).strip()
    collect_text = pytesseract.image_to_string(collect_clean, lang=lang, config=custom_config).strip()

    # Clean extracted text
    name_text = clean_ocr_output(name_text)
    collect_text = clean_ocr_output(collect_text)

    print(f"Extracted name: '{name_text}'")
    print(f"Extracted collect: '{collect_text}'")

    return name_text, collect_text

def clean_ocr_output(text):
    """Clean up OCR output by removing special characters and normalizing"""
    if not text:
        return ""

    # Remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters except for common card name characters
    text = re.sub(r'[^a-zA-Z0-9-:.,;()[]{}\'""?!&|_ ]', '', text)

    # Capitalize first letter of each word (for card names)
    text = re.sub(r'(^|\s)(\w)', lambda m: m.group(1) + m.group(2).upper(), text)

    # Remove leading/trailing spaces
    return text.strip()




# Common OCR substitutions map
OCR_SUBSTITUTIONS = {
    '0': 'O',
    '1': 'I',
    '3': 'E',
    '5': 'S',
    '7': 'T',
    '6': 'G',
    '8': 'B',
    '9': 'g',
    ' ': '',
    '|': 'I',
    '/': 'l',
    '!': 'I',
    'i': 'l',
    'j': 'i',
    '1': 'l',
    '3': 'e',
    '5': 's',
    '7': 't',
    '9': 'g',
    '@': 'a',
    '$': 's',
    '&': 'e',
    '(': 'c',
    ')': 'd',
    '[': 'c',
    ']': 'd',
    '{': 'c',
    '}': 'd',
    ';': 'l',
    ':': 'l',
    '*': 'x',
    '^': 'a',
    '~': 'n',
    '`': 'n',
    "'": '',
    '"': '',
    '?': 'q',
    '!': 'l',
    '%': 'x',
    '<': 'c',
    '>': 'd',
    ',': 'c',
    '.': 'e',
    '…': '...',
    '–': '-',
    '—': '-',
    '“': '',
    '”': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
    '‘': '',
    '’': '',
}

def normalize_ocr_text(text):
    """Normalize and correct common OCR errors"""
    if not text:
        return ""

    # Convert to lowercase for case-insensitive matching
    text = text.lower()

    # Replace common OCR errors with more likely characters
    for error, correct in OCR_SUBSTITUTIONS.items():
        text = text.replace(error, correct)

    # Remove multiple spaces and clean up
    text = re.sub(r'\s+', ' ', text).strip()

    # Common prefix/suffix patterns that often get misread
    text = re.sub(r'^the ', '', text)  # Many cards don't start with "the"
    text = re.sub(r' \& ', ' and ', text)
    text = re.sub(r' \+ ', ' plus ', text)
    text = re.sub(r' \- ', '-', text)
    text = re.sub(r' \( | \| ', '-', text)  # Common OCR for dashes

    # Remove extra apostrophes and quotes that often appear
    text = re.sub(r"['\"]", "", text)

    # Capitalize the first letter of each word (for card names)
    text = ' '.join(word.capitalize() for word in text.split())

    return text
