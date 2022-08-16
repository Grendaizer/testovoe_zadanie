import pytest
from selenium import webdriver
from source.settings import PATH


@pytest.fixture(autouse=False, scope='function')
def webdriver_driver():
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(time_to_wait=10)

    yield driver

    driver.quit()
