import streamlit as st
import time

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

def check_for_changes(driver, prev_texts):
    while True:
        driver.get("https://psyteam-fc61f.web.app/")
        
        # Extract the text content of the target elements
        xpath1 = "/html/body/div/main/div[2]/div[2]/div[1]/h2"
        xpath2 = "/html/body/div/main/div[2]/div[2]/div[2]/h2"
        
        element1 = driver.find_element(By.XPATH, xpath1)
        element2 = driver.find_element(By.XPATH, xpath2)
        
        text1 = element1.text
        text2 = element2.text
        
        if text1 != prev_texts[0] or text2 != prev_texts[1]:
            prev_texts[0] = text1
            prev_texts[1] = text2
            
            # Perform actions when text changes
            st.write("Text 1 changed:", text1)
            st.write("Text 2 changed:", text2)
            
            # Perform your get page source logic here
            # ...

        time.sleep(5)  # Wait for 10 seconds before checking again

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from lxml import html

    # @st.cache_resource
    def get_driver():
        x = ChromeDriverManager(driver_version="116.0.5845.96").install()
        service = Service(x)
        return webdriver.Chrome(service=service, options=options)

    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = get_driver()
    # driver.get("http://example.com")
    driver.get("https://psyteam-fc61f.web.app/")

    # st.code(driver.page_source)

    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Loding...')]")))
    driver.implicitly_wait(7)

    # Get the HTML content after the page has loaded
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content using lxml
    tree = html.fromstring(html_content)

    # Find all the text nodes using XPath
    text_nodes = tree.xpath("//text()")

    # Print each text node along with its parent element's XPath
    for node in text_nodes:
        # Get the parent element of the text node
        parent_element = node.getparent()

        if parent_element is not None:
            # Construct the XPath of the parent element
            parent_xpath = tree.getroottree().getpath(parent_element)
            
            # Strip and check if the text is not empty
            cleaned_text = node.strip()
            if cleaned_text:
                st.write("Text:", cleaned_text, "\nParent Element XPath:", parent_xpath)
    
    check_for_changes(driver)