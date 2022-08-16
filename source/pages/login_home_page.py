from selenium.webdriver.common.by import By


class Login_Home_Page:
    __EMAIL_ID = "mat-input-0"
    __PASSWORD_ID = "mat-input-1"
    __SIGN_IN_BUTTON = "/html/body/cm-root/ui-login-page/div[2]/div[3]/ui-auth-form/div[2]/div/div/form/div/button/div"

    def __init__(self, driver):
        self.driver = driver

    def do_some_with_mail(self, email1: str):
        email = self.driver.find_element(By.ID, self.__EMAIL_ID)
        email.send_keys(email1)

    def do_some_with_pass(self, pass1: str):
        password = self.driver.find_element(By.ID, self.__PASSWORD_ID)
        password.send_keys(pass1)

    def do_some_with_button(self):
        button = self.driver.find_element(By.XPATH, self.__SIGN_IN_BUTTON)
        button.click()
