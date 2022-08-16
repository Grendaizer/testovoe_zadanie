import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from source.pages.register_home_page import Register_Home_Page
from source.settings import URL, PATH, EMAIL, NAME, SECOND_NAME, PASSWORD


class Test_Register_Form:

    def test_emai_register(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(time_to_wait=10)
        try:
            self.driver.get(URL)
            register = Register_Home_Page(self.driver)
            register.send_name(NAME)
            register.send_last_name(SECOND_NAME)
            register.send_email(EMAIL)
            register.send_password(PASSWORD)
            register.click_checkbox()
            register.click_button()
            assert "The field cannot be empty" not in self.driver.page_source
            assert "Invalid email" not in self.driver.page_source
        finally:
            self.driver.quit()
