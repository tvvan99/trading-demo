from selenium.webdriver.common.by import By


class TradeLocators:
    STOPLOSS_INPUT = (By.CSS_SELECTOR, '[data-testid="trade-input-stoploss-price"]')
