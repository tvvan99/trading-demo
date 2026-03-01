import pytest
from page.google_homepage import GoogleHomePage
from action.search_actions import perform_search


def test_open_google(driver):
    page = GoogleHomePage(driver)
    page.load()
    assert "Google" in driver.title


def test_search_query(driver):
    perform_search(driver, "Selenium Python")
    assert "Selenium Python" in driver.title
