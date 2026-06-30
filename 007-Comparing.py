import pandas as pd

# Read both CSV files
solexs = pd.read_csv("solexsevents.csv")
hls = pd.read_csv("hel1osevents.csv")
print("SOLEXS Columns:")
print(solexs.columns)

print("HLS Columns:")
print(hls.columns)

# Convert time columns
solexs["Time"] = pd.to_datetime(
    solexs["Time"],
    format="%Y-%m-%d %H:%M:%S",
    errors="coerce"
)

hls["Time"] = pd.to_datetime(
    hls["Time"],
    format="%Y-%m-%d %H:%M:%S",
    errors="coerce"
)
print("First SOLEXS Time:", solexs["Time"].iloc[0])
print("First HLS Time:", hls["Time"].iloc[0])
print("SOLEXS")
print(solexs["Time"].head())

print("\nHLS")
print(hls["Time"].head())

print("="*70)
print("      SOLEXS vs HLS EVENT COMPARISON")
print("="*70)

for _, s in solexs.iterrows():

    print("\n")
    print(f"SOLEXS Event {s['Event']}")

    nearest_diff = None
    nearest_hls = None

    for _, h in hls.iterrows():

        diff = abs(s["Time"] - h["Time"])

        if nearest_diff is None or diff < nearest_diff:
            nearest_diff = diff
            nearest_hls = h

    print(f"SOLEXS Time : {s['Time']}")
    print(f"Nearest HLS : {nearest_hls['Time']}")
    print(f"Difference  : {nearest_diff}")
