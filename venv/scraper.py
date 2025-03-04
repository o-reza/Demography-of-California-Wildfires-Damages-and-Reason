from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--chromedriver_path', type=str, help="check where is the chromedriver in your pc")
args=parser.parse_args()

def main():
    url = "https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    webdriver_path = args.chromedriver_path  
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Wait for the button to be clickable
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")))
        print("Found the button!")
        button_click = driver.find_element(By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")
        button_click.click()
    except Exception as e:
        print(f"Error finding the button: {e}")

    # Wait for the table to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='alpha']")))

    # Find the <thead> and its <th> elements (headers)
    table_thead = driver.find_element(By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] thead")
    table_thead_th = table_thead.find_elements(By.TAG_NAME, "th")
    headers = [header.text for header in table_thead_th]

    # Initialize a list to store all data across pages
    all_table_data = []

    while True:
        # Find the <tbody> and its rows (<tr>)
        table_tbody = driver.find_element(By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] tbody")
        rows = table_tbody.find_elements(By.TAG_NAME, "tr")

        # Extract and append row data for this page
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text for cell in cells]
            all_table_data.append(row_data)

        # Try to extract the page info and print it for debugging
        try:
            page_info = driver.find_element(By.ID, "pageInfo").text
            print(f"Page Info: {page_info}")
        except:
            print("Error: Unable to find the page info.")
            page_info = ""  # If pageInfo isn't found, set it as empty

        if page_info.strip() == "":  # If we still have no page info
            print("No page info found, navigating using Next button directly.")
            # If no page info is available, try clicking the "Next" button until it's inactive
            next_button = driver.find_element(By.ID, "next")
            
            # Check if the "Next" button is disabled
            if "svelte-disabled" in next_button.get_attribute("class"):
                print("Next button is disabled, last page reached.")
                break  # Exit if the Next button is disabled (we're at the last page)

            # Wait until the next button is clickable
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(next_button))
            next_button.click()
        else:
            try:
                # Extract current page and total pages (e.g., "Page 1 of 4")
                current_page, total_pages = map(int, page_info.split(" ")[1::2])
                print(f"Current Page: {current_page}, Total Pages: {total_pages}")
            except ValueError:
                print(f"Error extracting page numbers from: {page_info}")
                break  # Exit if we can't extract page info

            # If we are on the last page, break out of the loop
            if current_page == total_pages:
                break
            
            # Click on the "Next" button
            next_button = driver.find_element(By.ID, "next")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(next_button)
            )
            next_button.click()

        # Wait for the page to reload and the table to refresh
        WebDriverWait(driver, 10).until(
            EC.staleness_of(table_tbody)  # Ensure the old table disappears
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] tbody"))
        )  # Ensure the new table appears

    # Create a pandas DataFrame from the collected data
    df = pd.DataFrame(all_table_data, columns=headers)

    # Print the DataFrame
    print("\nAll Data in tabular format:")
    print(df)

    # Optionally, save the DataFrame to a CSV file
    # df.to_csv('wildfire_data_all_pages.csv', index=False)

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()
