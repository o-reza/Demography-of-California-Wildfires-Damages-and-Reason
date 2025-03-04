# Demography-of-California-Wildfires-Damages-and-Reason

## Problem Statement
This project aims to gather data on the damages that happened due to the California Wildfire that occurred several times. Also from the extracted data the most dangerous Counties in California are tracked. 

We used the scrapped data to understand the following demographics:
-Total Acres Burned In California Wildfires in Different Years
-Deaths Count in California Wildfires & Risky Months of the Year 
-Fire Names that Burned Acres in California in Different Times
-Dollar Damage In California Due to Wildfires 
-Wildfires in California Due to Lighting & Acres Burned
-Human-Caused Wildfires in California & Acres Damage

The Website link we scrapped data from is [here](https://calmatters.org/california-wildfire-map-tracker/)

You can visit the Public Tableau Dashboard [here](https://public.tableau.com/app/profile/omar.reza/viz/DemographyofCaliforniaWildfiresDamagesReason/Dashboard1)  

## Build from sources and run scraper
1. Clone the repository
'''bash
git clone https://github.com/o-reza/Demography-of-California-Wildfires-Damages-and-Reason.git
'''
2. Initialize and activate virtual environment (for windows)
'''bash
virtualenv --no-site-packages venv
source venv/bin/activate
'''
3. Install dependencies
'''bash
pip install -r requirements.txt
'''
4. Download Chrome web driver from here: https://developer.chrome.com/docs/chromedriver/downloads
5. Run the scrapper
'''bash
python Tracking California wildfire/scraper.py --chromedrive_path <path-to-chromedriver>
'''
6. You will get CSV files with all fields with data, alternatively Check the scrapped data here:
    https://github.com/o-reza/Demography-of-California-Wildfires-Damages-and-Reason/blob/main/Tracking%20California%20Wildfire/acres_burned.csv 

Tableau public view: https://public.tableau.com/app/profile/omar.reza/viz/DemographyofCaliforniaWildfiresDamagesReason/Dashboard1 
