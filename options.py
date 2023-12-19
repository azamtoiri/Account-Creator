from selenium import webdriver
from data.links import user_agent
from fake_useragent import UserAgent

# fake user agent
ua = UserAgent()
useragent = ua.random

# Options
option = webdriver.ChromeOptions()

# User Agent
option.add_argument(
    f'User-Agent={user_agent}')

# WebDriver mode OFF
option.add_argument("--disable-blink-features=AutomationControlled")

# Drivers
driver = webdriver.Chrome("web-driver/chromedriver.exe", options=option)
