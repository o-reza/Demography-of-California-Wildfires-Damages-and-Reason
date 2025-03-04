from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    url = "https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    webdriver_path = r"C:\\Program Files (x86)\\chromedriver.exe"
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    driver.set_page_load_timeout(60)
    driver.get(url)

    # Corrected wait method
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")))
    
    print("found the button")
    return

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    url = "https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    
    # Set up Chrome options to run in headless mode
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no browser window)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    
    webdriver_path = r"C:\\Program Files (x86)\\chromedriver.exe"
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.set_page_load_timeout(120)  # Increased timeout to 120 seconds
    driver.get(url)

    # Wait for the button to appear
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")))

    print("found the button")

    # Additional operations can be performed here
    driver.quit()  # Close the browser

if __name__ == "__main__":
    main()
