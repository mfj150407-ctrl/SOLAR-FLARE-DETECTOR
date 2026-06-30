import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Read the SOLEXS CSV
solexs = pd.read_csv("solexs.csv")   # Change this to your actual CSV filename

# Take the first column as X and second column as Y
x = solexs.iloc[:, 0]
y = solexs.iloc[:, 1]

# Find peaks
peaks, properties = find_peaks(y, prominence=80,distance=300)#detct strongerand ignore closer peaks5

# Print peak information
print("Number of peaks found:", len(peaks))
print("\nPeak Locations:")

print("Number of peaks found:", len(peaks))

print("\nFirst 10 peaks:")
for i in peaks[:10]:
    print(f"X = {x.iloc[i]}, Y = {y.iloc[i]}")

# Plot the graph
plt.figure(figsize=(12,6))
plt.plot(x, y, label="SOLEXS Data")
plt.plot(x.iloc[peaks], y.iloc[peaks], "ro", label="Detected Peaks")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Solar Flare Peak Detection")
plt.legend()
plt.grid(True)

plt.show()
