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
            email = self.driver.find_element(By.ID, Login_Home_Page.EMAIL_ID)
            time.sleep(1)
            email.click()
            email.send_keys(EMAIL)
            time.sleep(1)
            password = self.driver.find_element(By.ID, Login_Home_Page.PASSWORD_ID)
            password.click()
            password.send_keys(PASSWORD)
            button = self.driver.find_element(By.XPATH,Login_Home_Page.SIGN_IN_BUTTOM)
            time.sleep(1)
            button.click()
        finally:
            self.driver.quit()