import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to get the driver
def get_driver():
    x = ChromeDriverManager(driver_version="116.0.5845.96").install()
    service = Service(x)
    return webdriver.Chrome(service=service, options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

chart = st.line_chart([], use_container_width=True)
temperature_values = []

def main():
    global chart
    global temperature_values
    st.title("Temperature Readings")
    st.write("Fetching temperature readings every 10 seconds")

    while True:
        driver = get_driver()
        driver.get("https://psyteam-fc61f.web.app/")
        driver.implicitly_wait(7)
        time.sleep(7)

        temperature_xpath = "/html/body/div/main/div[2]/div[2]/div[1]"
        target_temperature = driver.find_element("xpath", temperature_xpath)
        pure_temperature = float(str(target_temperature.text).split("\n")[1].replace("°C", "").strip())

        temperature_values.append(pure_temperature)

        chart.add_rows(data=pure_temperature)

        st.write("Last Fetched Temperature:", pure_temperature)

        driver.quit()

        # Wait for 10 seconds before fetching again
        time.sleep(3)

if __name__ == "__main__":
    main()
