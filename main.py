import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from data import links
from data.lists_NLO import combined_first_names_array, last_name_array
from options import driver, generate_password, alphabet

driver.get(f"{links.google_account}")

GMAIL_ADDR = None
# html = driver.find_element(By.TAG_NAME, "html")


def main():
    def click_next_button() -> None:
        """Click all next buttons on pages: clicking next button and wait 2 sec"""
        driver.find_element(By.CLASS_NAME, "VfPpkd-dgl2Hf-ppHlrf-sM5MNb").click()
        sleep(2)
    try:
        sleep(2)
        # get the firstname textbox
        first_name = driver.find_element(By.ID, "firstName")
        if first_name == None:
            raise ValueError("First name TextBox not found")
        first_name.clear()
        # generate first_name
        combined_first_names = (random.choice(combined_first_names_array))
        # enter first name
        first_name.send_keys(combined_first_names)

        # get the surname box
        surname = driver.find_element(By.ID, "lastName")
        surname.clear()
        # getting random last_name
        last_name = (random.choice(last_name_array))
        # enter surname
        surname.send_keys(last_name)

        # click next button
        click_next_button()

        # get day enter box
        day = driver.find_element(By.ID, "day")
        day.clear()
        # enter day
        day.send_keys((random.randint(1, 26)))

        # get month enter box
        month_dropdown = driver.find_element(By.ID, "month")
        month_select = Select(month_dropdown)
        month_select.select_by_index(random.randint(1, 12))

        # get year text box
        year_box = driver.find_element(By.ID, "year")
        year_box.clear()
        # enter year
        year_box.send_keys(random.randint(1968, 2003))

        # set male or femail
        male_or_female = driver.find_element(By.ID, "gender")
        male_or_female_select = Select(male_or_female)
        # setting male or female
        male_or_female_select.select_by_index(random.randint(1, 2))

        # click next button
        click_next_button()

        # choose own address and press next
        gmail_select = driver.find_element(By.ID, 'selectioni1')
        GMAIL_ADDR = gmail_select.text
        gmail_select.click()
        # click next button
        click_next_button()

        # get password textbox
        password = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Пароль"]')
        password.clear()
        # generate password
        mypw = generate_password(alphabet, 8)
        password.send_keys(mypw)

        # confirm password
        confirm_password = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Подтвердить"]')
        confirm_password.clear()
        confirm_password.send_keys(mypw)

        # click next button
        click_next_button()

    except Exception as ex:
        print(ex['args'])
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
