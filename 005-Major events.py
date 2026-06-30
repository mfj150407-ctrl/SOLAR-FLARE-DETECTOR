import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import matplotlib.dates as mdates

# ===============================
# Read the SOLEXS CSV
# ===============================
solexs = pd.read_csv("solexs.csv")# Change this to your CSV filename
print("Columns:")
print(solexs.columns)

print("\nFirst 5 rows:")
print(solexs.head())

print("\nFirst raw time value:")
print(solexs.iloc[0, 0])

print("\nData type:")
print(type(solexs.iloc[0, 0]))

# First column = X (Time/Index)
# Second column = Y (Intensity/Counts)
x = pd.to_datetime(solexs.iloc[:,0],unit='s')
y = solexs.iloc[:, 1]

# ===============================
# Detect Major Solar Flare Peaks
# ===============================
peaks, properties = find_peaks(
    y,
    prominence=100,     # Detect only major peaks
    distance=500        # Minimum separation between peaks
)

# ===============================
# Print Summary
# ===============================
print("=" * 60)
print("        SOLAR FLARE EVENT DETECTION REPORT")
print("=" * 60)

print(f"\nTotal Solar Flare Events Detected : {len(peaks)}\n")

print("{:<8} {:<18} {:<12}".format(
    "Event", "Time / X Value", "Intensity"))

print("-" * 45)
events=[]
for event_no, peak in enumerate(peaks, start=1):
    print("{:<8} {:<18} {:<12.2f}".format(
        event_no,
        x.iloc[peak].strftime("%Y-%m-%d %H:%M:%S"),
        y.iloc[peak]
    ))
    events.append({"Event":event_no,
                   "Time":x.iloc[peak].strftime("%Y-%m-%d %H:%M:%S"),
                   "Intensity":y.iloc[peak]})
                   
evesol=pd.DataFrame(events)
evesol.to_csv("solexsevents.csv",index=False)
print("table saved")
print("\nAnalysis Completed Successfully!")

# ===============================
# Plot Graph
# ===============================
plt.figure(figsize=(12,6))

plt.plot(
    x,
    y,
    color="blue",
    linewidth=1.5,
    label="SOLEXS Data"
)

plt.scatter(
    x.iloc[peaks],
    y.iloc[peaks],
    color="red",
    s=60,
    label="Detected Solar Flare"
)

plt.title("Solar Flare Peak Detection using SOLEXS Data", fontsize=15)
plt.xlabel("Time(UTC)")
plt.ylabel("X-Ray Intensity(counts)")
plt.grid(True)
plt.legend()
ax=plt.gca()
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
