from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

def main():
    url = "https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    webdriver_path = "C:\Program Files (x86)\chromedriver.exe"
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.d-button.dark[data-table='mu']")))
    button_click = driver.find_element(By.CSS_SELECTOR, "button.d-button.dark[data-table='mu']")
    button_click.click()

    # Wait for the table to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='mu']")))

    thead = driver.find_element(By.CSS_SELECTOR, "div.d-table-container[data-table='mu'] thead")
    thead_elements = thead.find_elements(By.TAG_NAME, "th")

    data = []

    # Loop through the pages and collect the data
    page_limit = 2  # Set the number of pages to scrape (you can adjust this)
    for page in range(page_limit):
        # Wait for table rows to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] tbody tr")))

        # Extract the rows from the current page
        rows = driver.find_elements(By.CSS_SELECTOR, "div.d-table-container[data-table='mu'] tbody tr")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            data.append([col.text for col in columns])

        # After extracting data, click the "Next" button to go to the next page
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='d-table-container'][@data-table='mu']//button[@id='next']"))
        )

        next_button.click()

        # Wait for the new data to load after clicking the "Next" button
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='mu'] tbody tr")))

    # Create a DataFrame with the scraped data
    df = pd.DataFrame(data, columns=[th.text for th in thead_elements])

    # Save the data to a CSV file
    df.to_csv("structure_damage_data.csv", index=False)

    driver.quit()

if __name__ == "__main__":
    main()
