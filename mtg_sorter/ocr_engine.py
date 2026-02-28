import cv2
import pytesseract


image_path = "./images/"


def extract_name(image_path, lang="eng"):
    img = cv2.imread(image_path)
    if img is None:
        return None, None

    # Advanced image enhancement
    img = enhance_card_image(img)
    
    h, w, _ = img.shape

    # Use optimized regions for better coverage
    name_roi = img[int(h * 0.05) : int(h * 0.14), int(w * 0.05) : int(w * 0.68)]
    collect_roi = img[int(h * 0.90) : int(h * 0.98), int(w * 0.05) : int(w * 0.38)]

    def clean_roi(roi):
        # Convert to grayscale with better contrast
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        
        # Advanced contrast enhancement
        gray = cv2.equalizeHist(gray)
        
        # Multiple preprocessing techniques for better OCR
        methods = []
        
        # Method 1: Binary thresholding with adaptive threshold
        _, binary_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        methods.append(binary_thresh)
        
        # Method 2: Adaptive thresholding (better for varying lighting)
        adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                               cv2.THRESH_BINARY_INV, 15, 3)
        methods.append(adaptive_thresh)
        
        # Method 3: CLAHE for better local contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced = clahe.apply(gray)
        _, clahe_thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        methods.append(clahe_thresh)
        
        # Method 4: Edge detection for text outlines
        edges = cv2.Canny(gray, 50, 150)
        methods.append(255 - edges)  # Invert edges
        
        # Combine all methods for maximum text detection
        combined = methods[0]  # Start with binary
        for method in methods[1:]:
            combined = cv2.bitwise_or(combined, method)
        
        # Advanced noise reduction
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        cleaned = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)
        
        return cleaned

    # Enhanced OCR configuration with multiple PSM modes
    def try_ocr_with_multiple_modes(roi, lang):
        modes = [7, 6, 11, 12, 8, 13]  # Different page segmentation modes
        results = []
        
        for mode in modes:
            try:
                text = pytesseract.image_to_string(
                    roi, lang=lang, config=f"--psm {mode}"
                ).strip()
                if text and len(text) > 1:  # Only keep meaningful results
                    results.append(text)
            except:
                continue
        
        # Return the longest result (most likely correct)
        return max(results, key=len) if results else ""

    name_text = try_ocr_with_multiple_modes(clean_roi(name_roi), lang)
    collect_text = try_ocr_with_multiple_modes(clean_roi(collect_roi), lang)

    return name_text, collect_text