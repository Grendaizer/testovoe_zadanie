import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from source.pages.login_home_page import Login_Home_Page
from source.pages.main_page import Main_Page
from source.settings import URL2, PATH, EMAIL, PASSWORD


class Test_Login_Form:

    def test_emai_login(self, webdriver_driver):
        webdriver_driver.get(URL2)
        login = Login_Home_Page(webdriver_driver)
        main = Main_Page(webdriver_driver)
        login.send_email(EMAIL)
        login.send_password(PASSWORD)
        login.click_button()
        assert "The field cannot be empty" not in webdriver_driver.page_source
        assert "Incorrect authentication credentials." not in webdriver_driver.page_source
        main.check_auth()
        print("\ntest finish")
