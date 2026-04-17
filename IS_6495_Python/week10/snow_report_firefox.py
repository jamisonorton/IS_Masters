from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

import time

browser_options = Options()
browser_options.add_argument("--headless")
s = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=s, options=browser_options)

driver.get("https://www.skiutah.com/members/snowbird/snowreport")

time.sleep(4)

overnight = driver.find_element(
    By.CSS_SELECTOR,
    "div.snowfall-item:nth-child(2) > dl:nth-child(1) > dd:nth-child(2)",
).get_attribute("innerHTML")
hour_24 = driver.find_element(
    By.CSS_SELECTOR, "div.col-md-6:nth-child(3) > dl:nth-child(1) > dd:nth-child(2)"
).get_attribute("innerHTML")
hour_48 = driver.find_element(
    By.CSS_SELECTOR, "div.col-4:nth-child(4) > dl:nth-child(1) > dd:nth-child(2)"
).get_attribute("innerHTML")

report = (
    f"Overnight snowfall: {overnight}," f"24 hours: {hour_24}," f"48 hours: {hour_48}"
)

print(report)
