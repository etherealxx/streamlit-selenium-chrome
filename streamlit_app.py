import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    # @st.cache_resource
    def get_driver():
        x = ChromeDriverManager(driver_version="116.0.5845.96").install()
        service = Service(x)
        return webdriver.Chrome(service=service, options=options)

    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = get_driver()
    driver.get("https://github.com/lushan88a/google_trans_new")
    data = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[2]/div[1]/h2/p').text

    st.write(data)
