import sys
import json
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]  # d:\Git\trading-demo
sys.path.insert(0, str(ROOT))

import pytest
from env.driver import create_driver
from page.login_page import LoginPage


@pytest.fixture(scope="session")
def driver(request):
    drv = create_driver()
    yield drv
    if request.session.testsfailed == 0:
        drv.quit()


@pytest.fixture(scope="session")
def logged_in_driver(driver):
    page = LoginPage(driver)
    page.load()
    page.login()
    yield driver


@pytest.fixture(scope="session")
def trade_data():
    data_path = ROOT / "test_data" / "trade_data.json"
    with open(data_path) as f:
        return json.load(f)
