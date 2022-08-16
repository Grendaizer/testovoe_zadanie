import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from source.pages.register_home_page import Register_Home_Page
from source.settings import URL, PATH, EMAIL, NAME, SECOND_NAME, PASSWORD


class Test_Register_Form:

    def test_emai_register(self):
        self.driver = webdriver.Chrome(PATH)
        try:
            self.driver.get(URL)
            time.sleep(1)
            register = Register_Home_Page(self.driver)
            register.send_name(NAME)
            time.sleep(1)
            register.send_last_name(SECOND_NAME)
            time.sleep(1)
            register.send_email(EMAIL)
            time.sleep(1)
            register.send_password(PASSWORD)
            time.sleep(1)
            register.click_checkbox()
            time.sleep(1)
            register.click_button()
            time.sleep(1)
        finally:
            self.driver.quit()
