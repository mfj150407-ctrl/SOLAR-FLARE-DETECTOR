import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import matplotlib.dates as mdates

# ====================================
# Read HLS CSV
# ====================================
hls = pd.read_csv("hel1os.csv")   # Change if your CSV name is different

# ====================================
# First column = Time
# Second column = Data
# ====================================
x=pd.to_datetime(hls["ISOT"])
print("Original ISOT:")
print(hls["ISOT"].head())

print("\nConverted x:")
print(x.head())
y=hls["CTR"]

# ====================================
# Detect Peaks
# ====================================
peaks, properties = find_peaks(
    y,
    prominence=100,
    distance=500
)

# ====================================
# Print Event Report
# ====================================
print("=" * 65)
print("             HLS EVENT DETECTION REPORT")
print("=" * 65)

print(f"\nTotal HLS Events Detected : {len(peaks)}\n")

print("{:<8} {:<25} {:<15}".format(
    "Event",
    "Time",
    "Intensity"
))

print("-" * 65)
events=[]
for event_no, peak in enumerate(peaks, start=1):
    print("{:<8} {:<25} {:<15.2f}".format(
        event_no,
        x.iloc[peak].strftime("%Y-%m-%d %H:%M:%S"),
        y.iloc[peak]
    ))
    events.append({"Event":event_no,
                   "Time":x.iloc[peak].strftime("%Y-%m-%d %H:%M:%S"),
                   "Intensity":y.iloc[peak]})
evehel=pd.DataFrame(events)
evehel.to_csv("hel1osevents.csv",index=False)
print("table saved")
                   
                   

print("\nAnalysis Completed Successfully!")

# ====================================
# Plot Graph
# ====================================
plt.figure(figsize=(12,6))

plt.plot(
    x,
    y,
    color="blue",
    linewidth=1.2,
    label="HLS Data"
)

plt.scatter(
    x.iloc[peaks],
    y.iloc[peaks],
    color="red",
    s=60,
    label="Detected HLS Events"
)

plt.title("HLS Event Detection - 02 February 2024")

plt.xlabel("Time")
plt.ylabel("HLS Intensity")

plt.grid(True)
plt.legend()
ax=plt.gca()
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
