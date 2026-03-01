from page.google_homepage import GoogleHomePage
from selenium.webdriver.remote.webdriver import WebDriver


def perform_search(driver: WebDriver, query: str):
    page = GoogleHomePage(driver)
    page.load()
    page.search(query)
