import time
from source.pages.register_home_page import Register_Home_Page
from source.settings import URL, EMAIL, NAME, SECOND_NAME, PASSWORD,TEST_EMAIL_URL


class Test_Register_Form:

    def test_email_register(self, webdriver_driver):
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
        assert "Please, verify your email address" in webdriver_driver.page_source
        re
        print("\ntest finish")
