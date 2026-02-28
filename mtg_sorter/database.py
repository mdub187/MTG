import json
import os
from difflib import get_close_matches


class CardDatabase:
    def __init__(self, json_path):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Database file {json_path} not found.")
            print(json_path)
        print(f"Loading {json_path} into memory...")
        with open(json_path, "r", encoding="utf-8") as f:
            all_cards = json.load(f)

        # Index: { "lowercasename": [list of card objects] }
        self.db = {}

        for card in all_cards:
            # 1. Index by English name (Oracle name)
            self._add_to_index(card.get("name"), card)

            # 2. Index by Printed name (French, etc.)
            # Scryfall uses 'printed_name' for non-English versions
            if "printed_name" in card:
                self._add_to_index(card.get("printed_name"), card)

        self.valid_names = list(self.db.keys())
        print(f"Database indexed with {len(self.valid_names)} unique name entries.")

    def _add_to_index(self, name, card_obj):
        """Helper to map a name to a list of card objects."""
        if not name:
            return
        key = name.lower().strip()
        if key not in self.db:
            self.db[key] = []
        self.db[key].append(card_obj)

    def find_best_match(self, ocr_name, collector_ocr="", min_confidence=0.75):
        if not ocr_name:
            return None, 0

        name_low = ocr_name.lower().strip()

        # Try exact match first
        if name_low in self.db:
            candidates = self.db[name_low]
        else:
            # Fuzzy match with adjustable confidence (supports OCR typos for both languages)
            match = get_close_matches(name_low, self.valid_names, n=1, cutoff=min_confidence)
            if not match:
                # Try with lower confidence if first attempt fails
                if min_confidence > 0.6:
                    return self.find_best_match(ocr_name, collector_ocr, min_confidence=0.6)
                return None, 0
            candidates = self.db[match[0]]

        # Use Collector Number/Set Code to narrow down if many printings exist
        if len(candidates) > 1 and collector_ocr:
            for c in candidates:
                set_code = c.get("set", "").lower()
                if set_code in collector_ocr.lower():
                    return self._format_result(c)

        # Fallback to the first match found
        return self._format_result(candidates[0])

    def _format_result(self, card_obj):
        """Returns a clean dictionary for your CSV."""
        return {
            "name": card_obj.get("name"),
            "printed_name": card_obj.get("printed_name", card_obj.get("name")),
            "lang": card_obj.get("lang", "unknown"),
            "set": card_obj.get("set_name"),
            "set_code": card_obj.get("set"),
            "price": card_obj.get("prices", {}).get("usd", "0.00"),
            "color": "".join(card_obj.get("color_identity", [])),
            "rarity": card_obj.get("rarity"),
        }
        self.__init__(CardDatabase)
