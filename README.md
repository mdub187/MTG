# MTG Sorter 

A Python-based Magic: The Gathering card sorting and identification tool.

Overview

MTG is a local utility that scans images of Magic: The Gathering cards, extracts card names using OCR, and matches them against a local Oracle card database. It is designed to help automate sorting large batches of physical cards by identifying them from photos.

The app loads a JSON card database into memory, scans specified image directories, attempts to identify each card, and reports results in the terminal.

Features
	•	Loads and indexes a full oracle_cards.json database
	•	Scans multiple image batch directories
	•	Performs OCR on card images to extract potential names
	•	Matches OCR results against indexed card names
	•	Reports unidentified cards with raw OCR output
	•	Designed for bulk card sorting workflows



The program will:
	1.	Load oracle_cards.json
	2.	Index all unique card names
	3.	Scan image directories
	4.	Attempt to identify each card
	5.	Output results to the terminal

Unidentified cards will display their filename and raw OCR text for debugging and tuning.

Notes
	•	OCR accuracy depends heavily on lighting, image clarity, and card positioning.
	•	Preprocessing images (cropping, contrast adjustments, resizing) can significantly improve identification rates.
	•	The Oracle database must be present and properly formatted as JSON.

Future Improvements
	•	Image preprocessing pipeline
	•	Fuzzy matching for OCR tolerance
	•	GUI for visual batch review
	•	Export results to CSV
	•	Automated sorting output directories
1.
Clone me
`
git clone https://github.com/mdub187/MTG.git
cd MTG
`
2.
Activate me
`
python -m venv .venv
source .venv/bin/activate
`
3.
My Requirements
`
pip install -r requirements.txt
`
4.
Add Cards
`
mtg_sorter/images/batch_one
mtg_sorter/images/batch_two
`
5.
Run Me
`
python __main__.py
`


License

MIT License
