import cv2
import pytesseract
import numpy as np
from PIL import Image, ImageEnhance


def get_roi_coords(img_width, img_height):
    """
    Calculate dynamic ROI coordinates based on image dimensions.
    Returns: dict with keys 'card_name' and 'collector_info'
    """
    return {
        "card_name": (
            int(img_width * 0.08), int(img_height * 0.05),
            int(img_width * 0.92), int(img_height * 0.12)
        ),
        "collector_info": (
            int(img_width * 0.75), int(img_height * 0.75),
            int(img_width * 0.98), int(img_height * 0.95)
        )
    }


def preprocess_image(img):
    """
    Apply contrast enhancement and deskew if needed.
    """
    # Convert to PIL for contrast enhancement
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    img_pil = ImageEnhance.Contrast(img_pil).enhance(1.5)
    img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    # Deskew logic (simplified - assumes small angles)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = np.column_stack(np.where(gray > 100))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return img


def extract_name(image_path):
    """
    Primary OCR function to get the card name and collector info.
    """
    img = cv2.imread(image_path)
    if img is None:
        return None, None

    h, w, _ = img.shape
    img = preprocess_image(img)

    # Get dynamic ROI coordinates
    rois = get_roi_coords(w, h)
    x1, y1, x2, y2 = rois["card_name"]
    name_roi = img[y1:y2, x1:x2]

    x1, y1, x2, y2 = rois["collector_info"]
    collect_roi = img[y1:y2, x1:x2]

    # Pre-processing (Grayscale + Threshold)
    def clean_roi(roi):
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        return thresh

    name_text = pytesseract.image_to_string(clean_roi(name_roi), lang="eng+fra", config="--psm 7").strip()
    collect_text = pytesseract.image_to_string(clean_roi(collect_roi), lang="eng+fra", config="--psm 7").strip()

    # Draw bounding boxes and text on the original image for visualization
    cv2.rectangle(img, (rois["card_name"][0], rois["card_name"][1]), (rois["card_name"][2], rois["card_name"][3]), (0, 255, 0), 2)
    cv2.rectangle(img, (rois["collector_info"][0], rois["collector_info"][1]), (rois["collector_info"][2], rois["collector_info"][3]), (0, 255, 0), 2)
    cv2.putText(img, name_text, (rois["card_name"][0], rois["card_name"][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(img, collect_text, (rois["collector_info"][0], rois["collector_info"][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image with bounding boxes and text
    # cv2.imshow('OCR Output', name_roi) # replace name_roi with img to see output of image
    # cv2.waitKey(0) # press any key to continue
    # cv2.destroyAllWindows()

    return name_text, collect_text
