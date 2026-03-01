from time import sleep

from locators.login_locators import LoginLocators
from config.settings import BASE_URL, LOGIN_USERNAME, LOGIN_PASSWORD
from page.base_page import BasePage


class LoginPage(BasePage):
    URL = BASE_URL

    def load(self):
        self.driver.get(self.URL)

    def login(self, username: str = LOGIN_USERNAME, password: str = LOGIN_PASSWORD):
        self.wait_for_element(LoginLocators.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element_clickable(LoginLocators.LOGIN_BUTTON).click()
        self.wait_for_url_contains("trade")
        self.wait_for_page_load()
