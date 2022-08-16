import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from source.pages.register_home_page import Register_Home_Page
from source.settings import URL, EMAIL, NAME, SECOND_NAME, PASSWORD


class Test_Register_Form:

    def test_email_register(self, webdriver_driver):
        try:
                webdriver_driver.get(URL)
                register = Register_Home_Page(webdriver_driver)
                register.send_name(NAME)
                register.send_last_name(SECOND_NAME)
                register.send_email(EMAIL)
                register.send_password(PASSWORD)
                register.click_checkbox()
                register.click_button()
                assert "The field cannot be empty" not in webdriver_driver.page_source
                assert "Invalid email" not in webdriver_driver.page_source
                assert "Please, verify your email address" not in webdriver_driver.page_source
        finally:
                print("\ntest finish")

