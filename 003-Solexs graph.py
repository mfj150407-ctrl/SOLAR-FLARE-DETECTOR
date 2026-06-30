import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
solexs = pd.read_csv("solexs.csv")
hls = pd.read_csv("hel1os.csv")

# Display column names
print("SOLEXS Columns:", solexs.columns)
print("HLS Columns:", hls.columns)

# Plot the second column against the first column
plt.figure(figsize=(10,5))
plt.plot(solexs.iloc[:,0], solexs.iloc[:,1], label="SOLEXS")
plt.xlabel("Energy (kev)")
plt.ylabel("Photon counts")
plt.title("SOLEXS Data")
plt.legend()
plt.grid(True)
plt.show()
