from selenium import webdriver
import pytest
from locators import MainPageLocators, AuthPageLocators
from linksst import LinksStorage
from logindata import UserProfile


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(LinksStorage.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.personal_account_btn).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(UserProfile.email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(UserProfile.password)
    driver.find_element(*AuthPageLocators.login_account_btn).click()

    return driver
