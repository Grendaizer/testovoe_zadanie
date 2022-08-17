import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Home_Page:
    __EMAIL_ID = "mat-input-0"
    __PASSWORD_ID = "mat-input-1"
    __SIGN_IN_BUTTON = "/html/body/cm-root/ui-login-page/div[2]/div[3]/ui-auth-form/div[2]/div/div/form/div/button/div"
    __MESSAGE = '//*[@id="cdk-overlay-17"]/snack-bar-container/div'

    def __init__(self, driver):
        self.driver = driver

    def send_email(self, email1: str):
        email = self.driver.find_element(By.ID, self.__EMAIL_ID)
        email.send_keys(email1)

    def send_password(self, pass1: str):
        password = self.driver.find_element(By.ID, self.__PASSWORD_ID)
        password.send_keys(pass1)

    def click_button(self):
        button = self.driver.find_element(By.XPATH, self.__SIGN_IN_BUTTON)
        button.click()

