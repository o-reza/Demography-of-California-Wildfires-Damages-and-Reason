# California-Wildfire-Analysis

## Problem Statement
California wildfires cause severe environmental and economic damage. This project analyzes wildfire data, including acres burned, fatalities, major incidents, financial losses, and causes to uncover key trends and impacts.

We used the scrapped data to understand the following demographics:
-Total Acres Burned In California Wildfires in Different Years
-Deaths Count in California Wildfires & Risky Months of the Year 
-Fire Names that Burned Acres in California in Different Times
-Dollar Damage In California Due to Wildfires 
-Wildfires in California Due to Lighting & Acres Burned
-Human-Caused Wildfires in California & Acres Damage

The Website link we scrapped data from is [here](https://calmatters.org/california-wildfire-map-tracker/)

You can visit the Public Tableau Dashboard [here](https://public.tableau.com/app/profile/omar.reza/viz/DemographyofCaliforniaWildfiresDamagesReason/Dashboard1)  

## Findings from the [Dashboard](https://public.tableau.com/app/profile/omar.reza/viz/DemographyofCaliforniaWildfiresDamagesReason/Dashboard1)
- Since 2025, the California wildfire caused the highest acres burned in 2020 (4304379 Acres)
- The November, 2018 Camp Fire is by far the most destructive wildfire in California that caused 85 (the highest death count) deaths
- The wildfire August Complex in 2020 burned the most number of acres in California (1032648 acres)
- Before 2025, the most expensive wildfire in California history was in 2017 that caused loss of USD:12,135,125,902
- Due to lighting the highest acres burned in California was in 2020 (2,932,231 acres)
- Human Caused Wildfires in California caused the highest acres burnt in 2018 (888760 acres)
  
## Build from sources and run python files
1. Clone the repository
'''bash
git clone https://github.com/o-reza/California-Wildfire-Analysis.git
'''
2. Initialize and activate virtual environment (for Windows)
'''bash
virtualenv --no-site-packages venv
source venv/bin/activate
'''
3. Install dependencies
'''bash
pip install -r requirements.txt
'''
4. Download Chrome web driver from here: https://developer.chrome.com/docs/chromedriver/downloads
5. Run the following python files & get csv files
'''bash
python California_Wildfires_Analysis/acres_burned.py --chromedrive_path <path-to-chromedriver>
'''

'''bash
python California_Wildfires_Analysis/acres_burned.py --chromedrive_path <path-to-chromedriver>
'''

'''bash
python California_Wildfires_Analysis/counties_affected.py --chromedrive_path <path-to-chromedriver>
'''

'''bash
python California_Wildfires_Analysis/deaths.py --chromedrive_path <path-to-chromedriver>
'''

'''bash
python California_Wildfires_Analysis/dollar_damage.py --chromedrive_path <path-to-chromedriver>
'''

'''bash
python California_Wildfires_Analysis/structure_damage.py --chromedrive_path <path-to-chromedriver>
'''

'''bash
python California_Wildfires_Analysis/fire_causes.py --chromedrive_path <path-to-chromedriver>
'''

7. You will get CSV files with all fields with data, alternatively Check the scrapped data here:
    https://github.com/o-reza/Demography-of-California-Wildfires-Damages-and-Reason/blob/main/Tracking%20California%20Wildfire/acres_burned.csv 

Tableau public view: https://public.tableau.com/app/profile/omar.reza/viz/DemographyofCaliforniaWildfiresDamagesReason/Dashboard1 
