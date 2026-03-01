from selenium.webdriver.remote.webdriver import WebDriver
from locators.google_locators import GoogleLocators


class GoogleHomePage:
    URL = "https://www.google.com"
    SEARCH_BOX = GoogleLocators.SEARCH_BOX

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, query: str):
        box = self.driver.find_element(*self.SEARCH_BOX)
        box.send_keys(query)
        box.submit()

    def open_and_search(self, query: str):
        self.load()
        self.search(query)
