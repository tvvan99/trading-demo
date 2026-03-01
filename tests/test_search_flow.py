from page.google_homepage import GoogleHomePage


def test_search_and_verify_results(driver, search_data):
    # perform a search and make sure the results page loads
    page = GoogleHomePage(driver)
    page.open_and_search(search_data["search_flow"])
    assert search_data["search_flow"] in driver.title.lower()


def test_search_box_still_visible(driver, search_data):
    # after search the search box should still be present on results page
    page = GoogleHomePage(driver)
    page.open_and_search(search_data["search_box_visible"])
    assert page.driver.find_element(*GoogleHomePage.SEARCH_BOX)
