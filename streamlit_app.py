import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Define the XPath expressions for the different text elements you want to scrape
xpaths = [
    "//h1",    # Example: <h1>...</h1>
    "//p",     # Example: <p>...</p>
    "//a",     # Example: <a>...</a>
    # Add more XPaths as needed
]

def get_driver():
    x = ChromeDriverManager(driver_version="116.0.5845.96").install()
    service = Service(x)
    return webdriver.Chrome(service=service, options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
driver.get("https://psyteam-fc61f.web.app/")

# Initialize an empty list to store scraped text
scraped_text = []

# Loop through the defined XPaths and extract text
for xpath in xpaths:
    elements = driver.find_elements_by_xpath(xpath)
    for element in elements:
        scraped_text.append(element.text)

# Display the scraped text in Streamlit
for text in scraped_text:
    st.write(text)
