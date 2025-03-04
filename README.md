# Demography-of-California-Wildfires-Damages-and-Reason

## Build from sources and run scrapper
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
