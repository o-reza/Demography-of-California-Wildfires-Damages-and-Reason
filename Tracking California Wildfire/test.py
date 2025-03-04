from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, ElementClickInterceptedException

def main():
    url = "https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    
    # Use raw string for the webdriver path to avoid the escape sequence warning
    webdriver_path = r"C:\Program Files (x86)\chromedriver.exe"
    
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)
        
        # Wait for the page to load fully and ensure the button is present
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")))
        
        # Print to confirm the button is located
        print("Button is located.")
        
        # Take a screenshot before clicking
        driver.save_screenshot("before_click.png")
        print("Screenshot taken: before_click.png")
        
        # Find the button element
        button_click = driver.find_element(By.CSS_SELECTOR, "button.d-button.dark[data-table='alpha']")
        
        # Scroll the button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", button_click)
        
        # Wait until the button is clickable
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button_click))
        
        # Attempt to click, handling any intercepted clicks
        try:
            button_click.click()
            print("Button clicked")
        except ElementClickInterceptedException:
            print("Element click intercepted, trying to click using JavaScript.")
            driver.execute_script("arguments[0].click();", button_click)
        
        # Give it a few seconds after clicking to allow the table to show up
        time.sleep(5)
        
        # Take a screenshot after clicking
        driver.save_screenshot("after_click.png")
        print("Screenshot taken: after_click.png")
        
        # Wait for the table to be visible after the button click
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='alpha']")))
        print("Table container visible")
        
        # Extract the table rows
        rows = driver.find_elements(By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] table tbody tr")
        
        # Print out the data for each row
        for row in rows:
            cols = row.find_elements(By.CSS_SELECTOR, "td")
            data = [col.text for col in cols]
            print(data)  # Print each row's data

    except TimeoutException as e:
        print(f"Timeout occurred: {e}")
    except InvalidSessionIdException as e:
        print(f"Browser session was closed unexpectedly: {e}")
    except ElementClickInterceptedException as e:
        print(f"Click intercepted exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Always quit the driver at the end
        driver.quit()

if __name__ == "__main__":
    main()
