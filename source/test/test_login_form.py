import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from source.pages.login_home_page import Login_Home_Page
from source.settings import URL2, PATH, EMAIL, PASSWORD


class Test_Login_Form:

    def test_emai_login(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(time_to_wait=10)
        try:
            self.driver.get(URL2)
            login = Login_Home_Page(self.driver)
            login.send_email(EMAIL)
            login.send_password(PASSWORD)
            login.click_button()
            assert "The field cannot be empty" not in self.driver.page_source
        finally:
            self.driver.quit()