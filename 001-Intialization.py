# ==========================================================
# Project : Solar Flare Forecasting using Aditya-L1
# Team    : Your Team Name
# Author  : Your Name
# ==========================================================

# ---------- Import Libraries ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

from astropy.io import fits

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

import warnings
warnings.filterwarnings("ignore")


# ==========================================================
# Step 1 : Read SoLEXS FITS File
# ==========================================================
# Automatically find any .lc file in the current folder
lc_files = glob.glob("*.lc")

if len(lc_files) == 0:
    print(" No SOLEXS .lc file found!")
    exit()

SOLEXS_FILE = lc_files[0]

print("Reading SoLEXS data...")
print("File Found:", SOLEXS_FILE)

solexs = fits.open(SOLEXS_FILE)

solexs.info()

solexs_data = solexs[1].data

solexs_df = pd.DataFrame(solexs_data)

print("\nSoLEXS Dataset")
print(solexs_df.head())

print("\nColumns")
print(solexs_df.columns)


# ==========================================================
# Step 2 : Read HEL1OS FITS File
# ==========================================================

fits_files = glob.glob("*.fits")

if len(fits_files) == 0:
    print("No HELIOS .fits file found!")
    exit()

HELIOS_FILE = fits_files[0]

print("\nReading HELIOS data...")
print("File Found:", HELIOS_FILE)

helios = fits.open(HELIOS_FILE)

helios.info()

helios_data = helios[1].data

helios_df = pd.DataFrame(helios_data)

print("\nHEL1OS Dataset")
print(helios_df.head())

print("\nColumns")
print(helios_df.columns)


# ==========================================================
# Step 3 : Save CSV Files
# ==========================================================

solexs_df.to_csv("solexs.csv", index=False)

helios_df.to_csv("hel1os.csv", index=False)

print("\nCSV files created successfully.")


# ==========================================================
# Step 4 : Close FITS files
# ==========================================================

solexs.close()
helios.close()

print("\nProject Initialized Successfully.")
