from selenium.webdriver.common.by import By


class Register_Home_Page:
    __First_Name_ID = 'mat-input-0'
    __Last_Name_ID = 'mat-input-1'
    __EMAIL_ID = "mat-input-2"
    __PASSWORD_ID = "mat-input-3"
    __CHECKBOX = "mat-checkbox-inner-container"
    __SIGN_UP_BUTTON = "/html/body/cm-root/ui-login-page/div[2]/div[3]/ui-registration-form/div[2]/div/div/form/div[5]/div"
    __SIGN_IN_BUTTOM = "/html/body/cm-root/ui-login-page/div[2]/div[3]/ui-auth-form/div[2]/div/div/form/div/button/div"

    def __init__(self, driver):
        self.driver = driver

    def do_some_with_name(self, name1: str):
        name = self.driver.find_element(By.ID, self.__First_Name_ID)
        name.send_keys(name1)

    def do_some_with_last_name(self, name2: str):
        last_name = self.driver.find_element(By.ID, self.__Last_Name_ID)
        last_name.send_keys(name2)

    def do_some_with_email(self, email1: str):
        email = self.driver.find_element(By.ID, self.__EMAIL_ID)
        email.send_keys(email1)
    def do_some_with_pass(self,password1:str):
        password = self.driver.find_element(By.ID, self.__PASSWORD_ID)
        password.send_keys(password1)

    def do_some_with_checkbox(self):
        checkbox = self.driver.find_element(By.CLASS_NAME, self.__CHECKBOX)
        checkbox.click()

    def do_some_with_button(self):
        button = self.driver.find_element(By.XPATH, self.__SIGN_UP_BUTTON)
        button.click()