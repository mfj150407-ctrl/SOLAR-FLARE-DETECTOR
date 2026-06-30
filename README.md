# SOLAR-FLARE-DETECTOR
This challenge is to build an automated algorithmic pipeline that uses the combined time-series data from SoLEXS and HEL1OS to detect (nowcast) or predict (forecast) these solar flares.
# Solar Flare Forecasting and Early Warning System

An AI-assisted Python project that analyzes solar observation data to detect and forecast potential solar flare events. The system automates the complete workflow—from data preprocessing and feature extraction to event detection, prediction, and early warning generation—using eight modular Python programs executed through a single master script.

## Features

* Automated execution using a master Python script
* Modular 8-stage processing pipeline
* Solar activity analysis and flare detection
* Early warning generation with event confirmation
* Easy to extend with additional datasets and prediction models

## Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* SciPy
* Astropy
* SunPy
* subprocess
* os
* glob
* seaborn
* scikit-learn
* requests

**Note:** This project was developed as a hackathon prototype for educational and research purposes and can be further enhanced with real-time satellite data and advanced machine learning models.

## Working
* As this program is fully under subprocesscontrols by accessing solar flare detector.py the entire program runs continuously
* Also for data interpretation we have uploaded a set of data for working process in case you need to access **PRADAN PORTAL OF ISRO**
* The particular links of those portal or given below
* https://pradan1.issdc.gov.in/al1/protected/browse.xhtml?id=solexs
* https://pradan1.issdc.gov.in/al1/protected/browse.xhtml?id=hel1os3
* you should choose data from the same date

*⚠️**DISCLAIMER**⚠️
    
    * My program needs to be in a separate folder where all the 9 python files must be present
    * Before this we should install modules using pip command where it goes like
           pip install numpy pandas matplotlib seaborn scikit-learn requests astropy sunpy scipy
    * Particularly my program needs only two data
           *AL1_SOLEXS_202XXXXX_SDD2_L1.lc(SOLEXS DATA WITH DATA)
           *lightcurve_cdte1.fits(HLS DATA)         
     * So extract these files particularly and update in same folder and you will witness wonders
          

 ## WORKFLOW PROCESS
 The system begins with initialization of raw satellite X-ray data, where soft and hard X-ray datasets are collected from the Aditya-L1 mission and converted into structured CSV files for processing. 

* Program 1: Loads and initializes the dataset, ensuring proper formatting and time-series alignment of the input data. 
* Program 2: Processes the first dataset (SoLEXS / soft X-ray CSV file) and generates a graphical representation of solar flux variations. 
* Program 3: Analyzes the plotted soft X-ray graph and identifies major peak points indicating possible solar activity variations. 
* Program 4: Consolidates the detected peak events from the soft X-ray data and stores them as key activity markers. 
* Program 5: Loads the second dataset (HEL1OS / hard X-ray data) and converts it into a graph-based visualization similar to the first dataset. 
* Program 6: Detects and marks major peak events in hard X-ray data, highlighting sudden energy bursts and flare-like signals. 
* Program 7: Compares both soft and hard X-ray results to identify common and significant event overlaps, improving confidence in detection. 
* Program 8: Consolidates all processed outputs and generates the final solar flare prediction result, indicating probable flare occurrence based on combined event analysis. 

The entire system runs as an automated sequential subprocess pipeline, where each program feeds output into the next stage without manual intervention, ensuring continuous analysis of solar activity data and that file is SOLAR FLARE DETECTOR.PY

