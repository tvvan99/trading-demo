from selenium.webdriver.common.by import By


class TradeLocators:

    # Order Type dropdown
    ORDER_TYPE_DROPDOWN = (By.CSS_SELECTOR, '[data-testid="trade-dropdown-order-type"]')

    # Order Type options (by visible text inside dropdown)
    ORDER_TYPE_MARKET     = (By.XPATH, '//*[@data-testid="trade-dropdown-order-type"]//following-sibling::*[contains(text(),"Market")]')
    ORDER_TYPE_LIMIT      = (By.XPATH, '//*[@data-testid="trade-dropdown-order-type"]//following-sibling::*[contains(text(),"Limit")]')
    ORDER_TYPE_STOP       = (By.XPATH, '//*[@data-testid="trade-dropdown-order-type"]//following-sibling::*[contains(text(),"Stop")]')

    # Volume / Units (shared across Market, Limit, Stop)
    VOLUME_INPUT          = (By.CSS_SELECTOR, '[data-testid="trade-input-volume"]')
    SWAP_TO_UNITS_BUTTON  = (By.CSS_SELECTOR, '[data-testid="trade-swap-to-units"]')

    # Fill Policy dropdown (shared across Market, Limit, Stop)
    # Market values : "Fill or Kill", "Immediate or Cancel"
    # Limit / Stop  : "Return"
    FILL_POLICY_DROPDOWN  = (By.CSS_SELECTOR, '[data-testid="trade-dropdown-fill-policy"]')

    # Limit / Stop order — price field (placeholder="$", name="price")
    LIMIT_STOP_PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')

    # Stop Loss (common across all order types)
    STOPLOSS_INPUT        = (By.CSS_SELECTOR, '[data-testid="trade-input-stoploss-price"]')

    # Take Profit (common across all order types)
    TAKEPROFIT_INPUT      = (By.CSS_SELECTOR, '[data-testid="trade-input-takeprofit-price"]')
