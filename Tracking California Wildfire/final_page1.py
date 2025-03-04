from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

def main():
    url="https://calmatters.org/california-wildfire-map-tracker/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfS4CG-Qk4fQSwk5ySvizY-3O19Q8aoNgLVKRs9YyAmd-QK2evxiS-saAgVBEALw_wcB"
    webdriver_path="C:\Program Files (x86)\chromedriver.exe"
    service=Service(webdriver_path)
    driver=webdriver.Chrome(service=service)
    driver.get(url)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.d-button.dark[data-table='alpha']")))
    button_click=driver.find_element(By.CSS_SELECTOR,"button.d-button.dark[data-table='alpha']")
    button_click.click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.d-table-container[data-table='alpha']")))
    thead=driver.find_element(By.CSS_SELECTOR,"div.d-table-container[data-table='alpha'] thead")
    thead_elements=thead.find_elements(By.TAG_NAME, "th")
    for th in thead_elements:
        print(th.text)
   
    data=[]
    rows=driver.find_elements(By.CSS_SELECTOR,"div.d-table-container[data-table='alpha'] tbody tr")
    for row in rows:
        columns=row.find_elements(By.TAG_NAME,"td")
        data.append([col.text for col in columns])
    df=pd.DataFrame(data, columns=[th.text for th in thead_elements])
    df.to_csv("wildfire_csv",index=False)
    #print(df)
    #driver.quit()
       # Use XPath to locate the "Next" button inside the specific parent div
    next_button = driver.find_element(By.XPATH, "//div[@class='d-table-container'][@data-table='alpha']//button[@id='next']")
    
    # Click the "Next" button
    next_button.click()

    # Wait for the new data to load after clicking the "Next" button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.d-table-container[data-table='alpha'] tbody tr")))
    print("gotta")


    return
if __name__=="__main__":
    main()