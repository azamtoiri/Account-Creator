import random

from fake_useragent import UserAgent
from selenium import webdriver

from data.links import user_agent

# fake user agent
ua = UserAgent()
useragent = ua.random

# Options
option = webdriver.ChromeOptions()

# User Agent
option.add_argument(
    f'User-Agent={user_agent}'
)

# WebDriver mode OFF
option.add_argument("--disable-blink-features=AutomationControlled")

# Drivers
driver = webdriver.Chrome("web-driver/chromedriver.exe", options=option)

alphabet = "abcdefghijklmnopqrstuvwxyz"

def generate_password(alphabet: str, pw_length: int) -> str:
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    # replace 1 or 2 characters with a number
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(mypw) // 2)
        mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index + 1:]

    # replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(mypw) // 2, len(mypw))
        mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index + 1:]

    return mypw
