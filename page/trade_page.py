import logging
from datetime import datetime

from selenium.webdriver.common.by import By

from locators.trade_locators import TradeLocators
from config.settings import BASE_URL, DEFAULT_ORDER_TYPE
from page.base_page import BasePage

from time import sleep

logger = logging.getLogger(__name__)


class _OrderForm(BasePage):
    """Shared volume / fill-policy behaviour for all order type forms."""

    def enter_volume(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.VOLUME_INPUT)
        field.click()
        field.clear()
        sleep(3)  # Temporary flaky fix
        field.send_keys(value)

    def get_volume_value(self) -> str:
        return self.wait_for_element(TradeLocators.VOLUME_INPUT).get_attribute("value")

    def swap_to_units(self):
        self.wait_for_element_clickable(TradeLocators.SWAP_TO_UNITS_BUTTON).click()

    def _select_fill_policy(self, value: str = None):
        if not value:
            return
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
        field = self.wait_for_element_clickable(TradeLocators.LIMIT_STOP_PRICE_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def get_price_value(self) -> str:
        return self.wait_for_element(TradeLocators.LIMIT_STOP_PRICE_INPUT).get_attribute("value")

    def select_expiry(self, value: str = None):
        if not value:
            return
        self.wait_for_element_clickable(TradeLocators.EXPIRY_DROPDOWN).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//*[normalize-space(text())="{value}"]')
        ).click()

    def enter_expiry_date(self, value: str):
        """value: date string, e.g. '2026-03-03'"""
        target = datetime.strptime(value, "%Y-%m-%d")
        self.wait_for_element_clickable(TradeLocators.EXPIRY_DATE_INPUT).click()
        self._navigate_calendar_to(target)
        aria_label = f"{target.strftime('%B')} {target.day}, {target.year}"
        self.wait_for_element_clickable(
            (By.XPATH, f'//abbr[@aria-label="{aria_label}"]')
        ).click()

    def _navigate_calendar_to(self, target: datetime):
        _MONTHS = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12,
        }
        while True:
            parts = self.wait_for_element(TradeLocators.EXPIRY_CALENDAR_LABEL).text.strip().split()
            cur_month, cur_year = _MONTHS[parts[0]], int(parts[1])
            if cur_year == target.year and cur_month == target.month:
                break
            if cur_year < target.year:
                self.wait_for_element_clickable(TradeLocators.EXPIRY_CALENDAR_NEXT_YEAR).click()
            elif cur_year > target.year:
                self.wait_for_element_clickable(TradeLocators.EXPIRY_CALENDAR_PREV_YEAR).click()
            elif cur_month < target.month:
                self.wait_for_element_clickable(TradeLocators.EXPIRY_CALENDAR_NEXT_MONTH).click()
            else:
                self.wait_for_element_clickable(TradeLocators.EXPIRY_CALENDAR_PREV_MONTH).click()

    def enter_expiry_time(self, value: str):
        """value: time string, e.g. '03:26'"""
        hour, minute = value.split(":")
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_INPUT).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_HOUR_TRIGGER).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//div[@data-testid="options"]//div[normalize-space(text())="{hour}"]')
        ).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_MINUTE_TRIGGER).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//div[@data-testid="options"]//div[normalize-space(text())="{minute}"]')
        ).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_OK).click()

    def clear_expiry_time(self):
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_INPUT).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_CLEAR).click()

    def select_fill_policy(self, value: str):
        self._select_fill_policy(value)


class StopOrderForm(LimitOrderForm):
    pass


class EditLimitOrderForm(LimitOrderForm):
    """LimitOrderForm with all locators scoped to #overlay-aqx-trader to avoid click interception."""

    def enter_price(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.EDIT_PRICE_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def get_price_value(self) -> str:
        return self.wait_for_element(TradeLocators.EDIT_PRICE_INPUT).get_attribute("value")

    def select_expiry(self, value: str = None):
        if not value:
            return
        self.wait_for_element_clickable(TradeLocators.EDIT_EXPIRY_DROPDOWN).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//*[normalize-space(text())="{value}"]')
        ).click()

    def enter_expiry_date(self, value: str):
        target = datetime.strptime(value, "%Y-%m-%d")
        self.wait_for_element_clickable(TradeLocators.EDIT_EXPIRY_DATE_INPUT).click()
        self._navigate_calendar_to(target)
        aria_label = f"{target.strftime('%B')} {target.day}, {target.year}"
        self.wait_for_element_clickable(
            (By.XPATH, f'//abbr[@aria-label="{aria_label}"]')
        ).click()

    def enter_expiry_time(self, value: str):
        hour, minute = value.split(":")
        self.wait_for_element_clickable(TradeLocators.EDIT_EXPIRY_TIME_INPUT).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_HOUR_TRIGGER).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//div[@data-testid="options"]//div[normalize-space(text())="{hour}"]')
        ).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_MINUTE_TRIGGER).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//div[@data-testid="options"]//div[normalize-space(text())="{minute}"]')
        ).click()
        self.wait_for_element_clickable(TradeLocators.EXPIRY_TIME_OK).click()

    def _select_fill_policy(self, value: str = None):
        if not value:
            return
        self.wait_for_element_clickable(TradeLocators.EDIT_FILL_POLICY_DROPDOWN).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//*[normalize-space(text())="{value}"]')
        ).click()

    def enter_stoploss_points(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.EDIT_STOPLOSS_POINTS_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def enter_takeprofit_points(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.EDIT_TAKEPROFIT_POINTS_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)


_BULK_CLOSE_CONFIRM = {
    "All Positions":        TradeLocators.BULK_CLOSE_CONFIRM_ALL,
    "Profitable Positions": TradeLocators.BULK_CLOSE_CONFIRM_PROFIT,
    "Loss Positions":       TradeLocators.BULK_CLOSE_CONFIRM_LOSS,
}

_BULK_CLOSE_CANCEL = {
    "All Positions":        TradeLocators.BULK_CLOSE_CANCEL_ALL,
    "Profitable Positions": TradeLocators.BULK_CLOSE_CANCEL_PROFIT,
    "Loss Positions":       TradeLocators.BULK_CLOSE_CANCEL_LOSS,
}

_ORDER_TYPE_FORMS = {
    "Market": MarketOrderForm,
    "Limit":  LimitOrderForm,
    "Stop":   StopOrderForm,
}


class TradePage(BasePage):
    URL = BASE_URL

    def load(self):
        self.driver.get(self.URL)

    def select_order_type(self, order_type: str = DEFAULT_ORDER_TYPE) -> _OrderForm:
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
        field = self.wait_for_element_clickable(TradeLocators.STOPLOSS_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def get_stoploss_value(self) -> str:
        return self.wait_for_element(TradeLocators.STOPLOSS_INPUT).get_attribute("value")

    def enter_stoploss_points(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.STOPLOSS_POINTS_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def get_stoploss_points_value(self) -> str:
        return self.wait_for_element(TradeLocators.STOPLOSS_POINTS_INPUT).get_attribute("value")

    # --- Take Profit ---
    def enter_takeprofit(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.TAKEPROFIT_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def get_takeprofit_value(self) -> str:
        return self.wait_for_element(TradeLocators.TAKEPROFIT_INPUT).get_attribute("value")

    def enter_takeprofit_points(self, value: str):
        field = self.wait_for_element_clickable(TradeLocators.TAKEPROFIT_POINTS_INPUT)
        field.click()
        field.clear()
        field.send_keys(value)

    def get_takeprofit_points_value(self) -> str:
        return self.wait_for_element(TradeLocators.TAKEPROFIT_POINTS_INPUT).get_attribute("value")

    # --- Pending orders tab ---
    def click_pending_orders_tab(self):
        self.wait_for_element_clickable(TradeLocators.PENDING_ORDERS_TAB).click()

    def get_latest_pending_order_id(self) -> str:
        return self.wait_for_element(
            (By.CSS_SELECTOR, '[data-testid="asset-pending-column-order-id"]')
        ).text.strip()

    def edit_pending_order(self, order_id: str) -> EditLimitOrderForm:
        self.wait_for_element_clickable((By.XPATH,
            f'//*[@data-testid="asset-pending-column-order-id" and normalize-space(text())="{order_id}"]'
            f'/ancestor::*[.//*[@data-testid="asset-open-button-edit"]][1]'
            f'//*[@data-testid="asset-open-button-edit"]'
        )).click()
        return EditLimitOrderForm(self.driver)

    # --- Open Trade button ---
    def click_open_trade(self):
        button = self.wait_for_element(TradeLocators.OPEN_TRADE_BUTTON)
        if button.text.strip() == "Market Closed":
            logger.warning("Open trade button is disabled: Market Closed")
            return
        button.click()

    # --- Trade confirmation dialog ---
    def confirm_trade(self):
        sleep(2) # Temporary flaky fix
        self.wait_for_element_clickable(TradeLocators.CONFIRM_BUTTON).click()

    def cancel_trade(self):
        sleep(2) # Temporary flaky fix
        self.wait_for_element_clickable(TradeLocators.CANCEL_BUTTON).click()

    # --- Bulk close ---
    def bulk_close_select_option(self, option: str):
        """Open the bulk-close dropdown and select an option.

        option: "All Positions", "Profitable Positions", or "Loss Positions"
        """
        self.wait_for_element_clickable(TradeLocators.BULK_CLOSE_DROPDOWN).click()
        self.wait_for_element_clickable(
            (By.XPATH, f'//*[normalize-space(text())="{option}"]')
        ).click()

    def bulk_close_confirm(self, option: str):
        sleep(2) # Temporary flaky fix
        self.wait_for_element_clickable(_BULK_CLOSE_CONFIRM[option]).click()

    def bulk_close_cancel(self, option: str):
        sleep(2) # Temporary flaky fix
        self.wait_for_element_clickable(_BULK_CLOSE_CANCEL[option]).click()
