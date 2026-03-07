# File: mtg_sorter_reflex/state.py

import reflex as rx
from .MTG_Sorter.ocr_engine import OCREngine
from .MTG_Sorter.database import CardDatabase
from typing import List, Dict
import os
import tempfile

# Initialize the card database once
db = CardDatabase

class OCRState(rx.State):
    uploaded_files: List[str] = []
    results: List[Dict] = []
    is_processing: bool = False
    error: str = ""
    temp_dir: str = tempfile.mkdtemp()

    def handle_upload(self, files: List[rx.UploadFile]):
        """Handle file uploads and store filenames."""
        self.uploaded_files = [file.filename for file in files]
        self.results = []
        self.error = ""
        yield  # Update UI immediately

    async def process_images(self):
        """Process uploaded images with OCR and database lookup."""
        if not self.uploaded_files:
            self.error = "No images uploaded!"
            return

        self.is_processing = True
        ocr = OCREngine()
        self.results = []

        for filename in self.uploaded_files:
            try:
                # Retrieve uploaded file data
                file_data = self.get_upload_data(filename)
                if not file_data:
                    continue

                # Save to temp file for OCR processing
                temp_path = os.path.join(self.temp_dir, filename)
                with open(temp_path, "wb") as f:
                    f.write(file_data)

                # Run OCR and database lookup
                raw_name, _ = ocr.extract_name(temp_path)
                match = db.find_best_match(raw_name)

                if match:
                    self.results.append({
                        "file": filename,
                        "name": match.get("name"),
                        "set": match.get("set"),
                        "color": match.get("color"),
                        "price": match.get("price"),
                        "rarity": match.get("rarity"),
                    })

                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)

            except Exception as e:
                self.error = f"Error processing {filename}: {str(e)}"
                self.is_processing = False
                return

        self.is_processing = False

    def get_upload_data(self, filename: str) -> bytes:
        """Retrieve uploaded file data by filename."""
        for uploaded_file in rx.get_upload_files():
            if uploaded_file.filename == filename:
                return uploaded_file.read()
        return b""

    def clear_results(self):
        """Clear results and uploaded files."""
        self.uploaded_files = []
        self.results = []
        self.error = ""

    def export_to_csv(self):
        """Export results to CSV."""
        if not self.results:
            return rx.window_alert("No results to export!")

        csv_data = "\n".join([
            "File,Card Name,Set,Color,Price,Rarity",
            *[
                f"{r['file']},{r['name']},{r['set']},{r['color']},{r['price']},{r['rarity']}"
                for r in self.results
            ],
        ])

        return rx.download(
            filename="inventory.csv",
            data=csv_data,
            mime_type="text/csv",
        )
