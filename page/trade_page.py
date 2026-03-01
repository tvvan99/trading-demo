from locators.trade_locators import TradeLocators
from config.settings import BASE_URL
from page.base_page import BasePage

from time import sleep


class TradePage(BasePage):
    URL = BASE_URL

    def load(self):
        self.driver.get(self.URL)

    def enter_stoploss(self, value: str):
        field = self.wait_for_element(TradeLocators.STOPLOSS_INPUT)
        field.clear()
        field.send_keys(value)
        sleep(5)

    def get_stoploss_value(self) -> str:
        return self.wait_for_element(TradeLocators.STOPLOSS_INPUT).get_attribute("value")
