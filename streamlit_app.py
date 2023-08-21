import streamlit as st
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html

def get_driver():
    x = ChromeDriverManager(driver_version="116.0.5845.96").install()
    service = Service(x)
    return webdriver.Chrome(service=service, options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

st.title("Temperature Monitoring")

# Initialize an empty list to store temperature data
temperature_data = []

while True:
    driver = get_driver()
    driver.get("https://psyteam-fc61f.web.app/")

    driver.implicitly_wait(7)
    time.sleep(7)

    temperature_xpath = "/html/body/div/main/div[2]/div[2]/div[1]"
    condition_xpath = "/html/body/div/main/div[2]/div[2]/div[2]"

    try:
        target_temperature = driver.find_element(By.XPATH, temperature_xpath)
        target_condition = driver.find_element(By.XPATH, condition_xpath)
        temperature_data.append((time.time(), float(target_temperature.text)))
        
        st.write("Temperature:", target_temperature.text)
        st.write("Condition:", target_condition.text)
        
        # Plot the data using st.line_chart
        if temperature_data:
            timestamps, temperatures = zip(*temperature_data)
            st.line_chart({"Timestamps": timestamps, "Temperature": temperatures})
        
    except Exception as e:
        st.write("Error:", e)
        
    driver.quit()
    
    # Wait for 10 seconds before fetching data again
    time.sleep(3)
