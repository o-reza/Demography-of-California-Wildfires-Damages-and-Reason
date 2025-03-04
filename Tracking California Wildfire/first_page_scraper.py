from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

def main():
    url = "https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    webdriver_path = r"C:\Program Files (x86)\chromedriver.exe"  # Fixed path format
    
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    # Wait for the button to load and click
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")))
    print("Button found")
    
    button_click = driver.find_element(By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")
    button_click.click()

    # Wait for the table to load after clicking
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] tbody tr")))

    # Extract header names
    table_thead = driver.find_element(By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] thead")
    table_thead_th = table_thead.find_elements(By.TAG_NAME, "th")
    headers = [header.text for header in table_thead_th]

    # Extract row data
    table_tbody = driver.find_element(By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] tbody")
    rows = table_tbody.find_elements(By.TAG_NAME, "tr")

    table_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        table_data.append(row_data)

    # Create DataFrame
    df = pd.DataFrame(table_data, columns=headers)

    print("\nData in tabular format:")
    print(df)

    # Optionally, save the DataFrame to CSV
    # df.to_csv('wildfire_data.csv', index=False)

    driver.quit()

if __name__ == "__main__":
    main()
