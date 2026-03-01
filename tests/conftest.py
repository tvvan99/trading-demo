import sys
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]  # d:\Git\trading-demo
sys.path.insert(0, str(ROOT))

import pytest
from env.driver import create_driver


@pytest.fixture(scope="session")
def driver():
    drv = create_driver(headless=False)
    yield drv
    drv.quit()
