import requests
import time


def download_scryfall_bulk():
    # Scryfall REQUIRES a User-Agent header or they may block the request
    headers = {"User-Agent": "MTGSorter/1.0", "Accept": "application/json"}
    url = "https://api.scryfall.com/bulk-data/oracle-cards"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will catch 404/429/500 errors
        bulk_meta = response.json()

        if "download_uri" in bulk_meta:
            download_url = bulk_meta["download_uri"]
            print(f"Downloading from: {download_url}")

            # Streaming download for large files
            r = requests.get(download_url, headers=headers, stream=True)
            
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    download_scryfall_bulk()
    # Scryfall REQUIRES a User-Agent header or they may block the request
    headers = {"User-Agent": "MTGSorter/1.0", "Accept": "application/json"}
    url = "https://api.scryfall.com/bulk-data/oracle-cards"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will catch 404/429/500 errors
        bulk_meta = response.json()

        if "download_uri" in bulk_meta:
            download_url = bulk_meta["download_uri"]
            print(f"Downloading from: {download_url}")

            # Streaming download for large files
            r = requests.get(download_url, headers=headers, stream=True)
            with open("oracle_cards.json", "w") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Download complete.")
        else:
            print(f"Unexpected API response: {bulk_meta}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to reach Scryfall: {e}")
