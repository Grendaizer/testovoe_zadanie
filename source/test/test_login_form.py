import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from source.pages.login_home_page import Login_Home_Page
from source.settings import URL2, PATH, EMAIL, PASSWORD


class Test_Login_Form:

    def test_emai_login(self):
        self.driver = webdriver.Chrome(PATH)
        try:
            self.driver.get(URL2)
            time.sleep(2)
            login = Login_Home_Page(self.driver)
            time.sleep(1)
            login.send_email(EMAIL)
            time.sleep(1)
            login.send_password(PASSWORD)
            time.sleep(1)
            login.click_button()
            time.sleep(1)
        finally:
            self.driver.quit()