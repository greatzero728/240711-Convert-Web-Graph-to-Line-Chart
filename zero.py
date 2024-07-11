from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Set up the Chrome WebDriver service
service = Service(r'C:\Users\Zero To Hero\.cache\selenium\chromedriver\win64\126.0.6478.126\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the web page
driver.get('https://notice.co/c/rubrik/chart?t=max')

# Allow time for the page to load and for data to be rendered
time.sleep(10)  # Adjust the sleep time if necessary

try:
    # Wait for the canvas element to be present
    canvas = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas[role="figure"]'))
    )

    # Extract the data points (this part depends on how the data is structured in the canvas)
    data_script = '''
    return document.querySelector('canvas').__chartist__.data.series;
    '''
    data = driver.execute_script(data_script)

    # Process and save the data to a CSV file
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Price"])
        for point in data[0]:  # Adjust according to the data structure
            writer.writerow(point)

    print("Data extraction complete.")
    
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the browser
    driver.quit()
