from data import links

from time import sleep
from options import driver
from selenium.webdriver.common.by import By

from data.buttons_xpath import *

driver.get(f"{links.google_account2}")

html = driver.find_element(By.TAG_NAME, "html")


def main():
    try:
        sleep(2)
        # driver.find_element(By.TAG_NAME, "use").click()

        driver.find_element(By.XPATH, b_create_account).click()

        driver.find_element(By.XPATH, b_create_account_for_myself).click()

        driver.find_element(By.XPATH, b_input_firstName).send_keys("lsdkfj;lasdfj;lasd")

        driver.find_element(By.XPATH, b_input_lastName).send_keys("sldfjsldfj")

        driver.find_element(By.XPATH, b_username).send_keys("sdlkfjlkasd")

        driver.find_element(By.XPATH, b_password).send_keys("SDLfjsdlkjf;lasdjf")
        driver.find_element(By.XPATH, b_confirm_password).send_keys("SDLfjsdlkjf;lasdjf")
        driver.find_element(By.XPATH, b_next_1).click()
        sleep(2)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
