import pandas as pd

# Read event tables
solexs = pd.read_csv("solexsevents.csv")
hls = pd.read_csv("hel1osevents.csv")

# Convert Time column to datetime
solexs["Time"] = pd.to_datetime(solexs["Time"])
hls["Time"] = pd.to_datetime(hls["Time"])

confirmed = 0
possible = 0
rejected = 0

print("=" * 60)
print("        SOLAR FLARE EARLY WARNING SYSTEM")
print("=" * 60)

confirmed_times=[]

for _, s in solexs.iterrows():

    # Find nearest HLS event
    diff = abs(hls["Time"] - s["Time"])
    nearest = diff.idxmin()

    hls_time = hls.loc[nearest, "Time"]
    difference = diff.min()

    minutes = difference.total_seconds() / 60


    if minutes <= 5:
        status = "CONFIRMED SOLAR FLARE"
        recommendation = "Issue Space Weather Alert"
        confirmed += 1
        confirmed_times.append(s["Time"])

    elif minutes <= 15:
        status = "POSSIBLE SOLAR FLARE"
        recommendation = "Monitor Continuously"
        possible += 1

    else:
        status = "NO CONFIRMATION"
        recommendation = "No Alert Required"
        rejected += 1

    print("\n" + "-" * 60)
    print(f"SOLEXS Event : {int(s['Event'])}")
    print(f"SOLEXS Time  : {s['Time']}")
    print(f"HLS Time     : {hls_time}")
    print(f"Difference   : {difference}")
    print(f"STATUS       : {status}")
    print(f"ACTION       : {recommendation}")

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)
print(f"SOLEXS Events      : {len(solexs)}")
print(f"HLS Events         : {len(hls)}")
print(f"Confirmed Events   : {confirmed}")
print(f"Possible Events    : {possible}")
print(f"Rejected Events    : {rejected}")

if confirmed > 0:
    print("\nFINAL RESULT : SOLAR FLARE DETECTED")
    print("ALERT LEVEL  : HIGH")

    print("\nConfirmed Solar Flare Time(s):")
    for t in confirmed_times:
        print("•", t)
elif possible > 0:
    print("\nFINAL RESULT : POSSIBLE SOLAR FLARE")
    print("ALERT LEVEL  : MEDIUM")
else:
    print("\nFINAL RESULT : NO SIGNIFICANT SOLAR FLARE")
    print("ALERT LEVEL  : LOW")

print("=" * 60)
