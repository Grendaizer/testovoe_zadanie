from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_Page():
    __MESSAGE = 'search-wrapper'

    def __init__(self, driver):
        self.driver = driver

    def check_auth(self):
        self.driver.find_element(By.CLASS_NAME, self.__MESSAGE)

