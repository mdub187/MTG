import os
import pandas as pd
from pathlib import Path
csv_path = Path("")
if __name__ == "__main__":
	path_to_csv = os.path.abspath(
		csv_path
	)
	df = pd.read_csv(f'{path_to_csv}/card_results.csv')
	df2 = pd.read_csv(f'{path_to_csv}/french_inventory.csv')
	df3 = pd.read_csv(f'{path_to_csv}/master_inventory.csv')
	# df = pd.read_csv() . .
	print(df.head())

	total = [df["Price_USD"].sum() ++ df2["Price_USD"].sum() ++ df3["Price_USD"].sum()]
	print(total)
