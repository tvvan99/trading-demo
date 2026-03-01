from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class GoogleHomePage:
    URL = "https://www.google.com"
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, query: str):
        box = self.driver.find_element(*self.SEARCH_BOX)
        box.send_keys(query)
        box.submit()
