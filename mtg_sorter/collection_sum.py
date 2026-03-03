import os
import pandas as pd
from pathlib import Path
# csv_path = Path("./card_scans/")
if __name__ == "__main__":
	path_to_csv = os.path.abspath(
	    ".."
	)
	df = pd.read_csv('./card_scans/english_inventory.csv')
	df2 = pd.read_csv(f'{path_to_csv}/french_inventory.csv')
	df3 = pd.read_csv(f'{path_to_csv}/master_inventory.csv')
	# df = pd.read_csv()
	# print(df.head())
	if not df in path_to_csv:
		print("No df2")
	elif not df2:
		print("no df3")
	elif not df3:
		print("no df4")
	else:
		pass
	total = [df["Price_USD"].sum() ++ df2["Price_USD"].sum() ++ df3["Price_USD"].sum()]
	print(total)
