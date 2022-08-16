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
            name1 = self.driver.find_element(By.ID, Register_Home_Page.First_Name_ID)
            time.sleep(1)
            name1.send_keys(NAME)
            time.sleep(1)
            name2 = self.driver.find_element(By.ID, Register_Home_Page.Last_Name_ID)
            time.sleep(1)
            name2.click()
            name2.send_keys(SECOND_NAME)
            time.sleep(1)
            email = self.driver.find_element(By.ID, Register_Home_Page.EMAIL_ID)
            time.sleep(1)
            email.click()
            email.send_keys(EMAIL)
            time.sleep(1)
            password = self.driver.find_element(By.ID, Register_Home_Page.PASSWORD_ID)
            password.click()
            password.send_keys(PASSWORD)
            galochka = self.driver.find_element(By.CLASS_NAME, Register_Home_Page.CHECKBOX)
            time.sleep(1)
            galochka.click()
            time.sleep(1)
            button = self.driver.find_element(By.XPATH, Register_Home_Page.SIGN_UP_BUTTON)
            time.sleep(1)
            button.click()
        finally:
            self.driver.quit()
