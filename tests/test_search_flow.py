from action.search_actions import perform_search
from page.google_homepage import GoogleHomePage


def test_search_and_verify_results(driver):
    # perform a search and make sure the results page loads
    perform_search(driver, "python automation")
    assert "python automation" in driver.title.lower()


def test_search_box_still_visible(driver):
    # after search the search box should still be present on results page
    perform_search(driver, "selenium webdriver")
    page = GoogleHomePage(driver)
    # reuse the page object to check elements exist
    assert page.driver.find_element(*GoogleHomePage.SEARCH_BOX)
