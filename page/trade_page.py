from selenium.webdriver.common.by import By

from locators.trade_locators import TradeLocators
from config.settings import BASE_URL
from page.base_page import BasePage

from time import sleep


class _OrderForm(BasePage):
    """Shared volume / fill-policy behaviour for all order type forms."""

    def enter_volume(self, value: str):
        field = self.wait_for_element(TradeLocators.VOLUME_INPUT)
        field.clear()
        field.send_keys(value)

    def get_volume_value(self) -> str:
        return self.wait_for_element(TradeLocators.VOLUME_INPUT).get_attribute("value")

    def swap_to_units(self):
        self.wait_for_element_clickable(TradeLocators.SWAP_TO_UNITS_BUTTON).click()

    def _select_fill_policy(self, value: str):
        self.wait_for_element_clickable(TradeLocators.FILL_POLICY_DROPDOWN).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//*[normalize-space(text())="{value}"]')
        ).click()


class MarketOrderForm(_OrderForm):
    FILL_OR_KILL = "Fill or Kill"
    IMMEDIATE_OR_CANCEL = "Immediate or Cancel"

    def select_fill_policy(self, value: str):
        """value: MarketOrderForm.FILL_OR_KILL or MarketOrderForm.IMMEDIATE_OR_CANCEL"""
        self._select_fill_policy(value)


class LimitOrderForm(_OrderForm):
    def enter_price(self, value: str):
        field = self.wait_for_element(TradeLocators.LIMIT_STOP_PRICE_INPUT)
        field.clear()
        field.send_keys(value)

    def get_price_value(self) -> str:
        return self.wait_for_element(TradeLocators.LIMIT_STOP_PRICE_INPUT).get_attribute("value")

    def select_fill_policy(self):
        self._select_fill_policy("Return")


class StopOrderForm(LimitOrderForm):
    pass


_ORDER_TYPE_FORMS = {
    "Market": MarketOrderForm,
    "Limit":  LimitOrderForm,
    "Stop":   StopOrderForm,
}


class TradePage(BasePage):
    URL = BASE_URL

    def load(self):
        self.driver.get(self.URL)

    def select_order_type(self, order_type: str) -> _OrderForm:
        """Open the Order Type dropdown, select an option, and return the matching form object.

        Supported values: "Market", "Limit", "Stop"
        """
        self.wait_for_element_clickable(TradeLocators.ORDER_TYPE_DROPDOWN).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//*[normalize-space(text())="{order_type}"]')
        ).click()
        return _ORDER_TYPE_FORMS[order_type](self.driver)

    # --- Stop Loss ---
    def enter_stoploss(self, value: str):
        field = self.wait_for_element(TradeLocators.STOPLOSS_INPUT)
        field.clear()
        field.send_keys(value)
        sleep(5)

    def get_stoploss_value(self) -> str:
        return self.wait_for_element(TradeLocators.STOPLOSS_INPUT).get_attribute("value")

    # --- Take Profit ---
    def enter_takeprofit(self, value: str):
        field = self.wait_for_element(TradeLocators.TAKEPROFIT_INPUT)
        field.clear()
        field.send_keys(value)

    def get_takeprofit_value(self) -> str:
        return self.wait_for_element(TradeLocators.TAKEPROFIT_INPUT).get_attribute("value")
