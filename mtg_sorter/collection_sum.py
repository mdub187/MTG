import os
import pandas as pd

path = "./french_inventory.csv"
if __name__ == "__main__":
	path_to_csv = os.path.abspath(
		path
	)
	df = pd.read_csv("../card_results.csv")
	df2 = pd.read_csv("../french_inventory.csv")
	df3 = pd.read_csv("../master_inventory.csv")
	# df = pd.read_csv() . .
	print(df.head())

	total = [df["Price_USD"].sum() + df2["Price_USD"].sum() + df3["Price_USD"].sum()]
	print(total)
