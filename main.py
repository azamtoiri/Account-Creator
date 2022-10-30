from time import sleep
from options import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("https://www.google.com/account/about/")
html = driver.find_element(By.TAG_NAME, "html")

# region: Buttons: account details
b_create_account = '//*[@id="h-js-header__drawer"]/div[2]/ul/li[1]/a'
b_input_firstName = '//*[@id="firstName"]'
b_input_lastName = '//*[@id="lastName"]'
b_username = '//*[@id="username"]'
b_password = '//*[@id="passwd"]/div[1]/div/div[1]/input'
b_confirm_password = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'
b_next_1 = '//*[@id="accountDetailsNext"]/div/button/span'
# endregion


def main():
    try:
        sleep(2)
        driver.find_element(By.TAG_NAME, "use").click()

        driver.find_element(By.XPATH, b_create_account).click()

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
