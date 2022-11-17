from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent

# fake user agent
ua = UserAgent()
useragent = ua.random

# Options
option = webdriver.ChromeOptions()

# User Agent
option.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
    'Safari/537.36')

# WebDriver mode OFF
option.add_argument("--disable-blink-features=AutomationControlled")

# Drivers
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=option)
