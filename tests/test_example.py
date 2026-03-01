from page.google_homepage import GoogleHomePage


def test_open_google(driver, search_data):
    page = GoogleHomePage(driver)
    page.load()
    assert search_data["open_google"] in driver.title


def test_search_query(driver, search_data):
    page = GoogleHomePage(driver)
    page.open_and_search(search_data["search_query"])
    assert search_data["search_query"] in driver.title
