import pandas as pd

# Read the CSV files
solexs = pd.read_csv("solexs.csv")
hls = pd.read_csv("hel1os.csv")

# Display the first 5 rows
print("SOLEXS Data:")
print(solexs.head())

print("\nHLS Data:")
print(hls.head())
