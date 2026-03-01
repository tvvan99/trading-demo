from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config.settings import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, locator: tuple, timeout: int = WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator: tuple, timeout: int = WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, text: str, timeout: int = WAIT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    def wait_for_page_load(self, timeout: int = WAIT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def js_click(self, locator: tuple, timeout: int = WAIT_TIMEOUT):
        element = self.wait_for_element_clickable(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def action_click(self, locator: tuple, timeout: int = WAIT_TIMEOUT):
        element = self.wait_for_element_clickable(locator, timeout)
        ActionChains(self.driver).move_to_element(element).click().perform()
