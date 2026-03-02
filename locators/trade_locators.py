from selenium.webdriver.common.by import By


class TradeLocators:

    # Order Type dropdown
    ORDER_TYPE_DROPDOWN = (By.CSS_SELECTOR, '[data-testid="trade-dropdown-order-type"]')

    # Volume / Units (shared across Market, Limit, Stop)
    VOLUME_INPUT          = (By.CSS_SELECTOR, '[data-testid="trade-input-volume"]')
    SWAP_TO_UNITS_BUTTON  = (By.CSS_SELECTOR, '[data-testid="trade-swap-to-units"]')

    # Fill Policy dropdown (shared across Market, Limit, Stop)
    # Market values : "Fill or Kill", "Immediate or Cancel"
    # Limit / Stop  : "Return"
    FILL_POLICY_DROPDOWN  = (By.CSS_SELECTOR, '[data-testid="trade-dropdown-fill-policy"]')

    # Limit / Stop order — price field (placeholder="$", name="price")
    LIMIT_STOP_PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')

    # Limit / Stop order — expiry dropdown
    # Options: "Good Till Canceled", "Good Till Day", "Specified Date", "Specified Date and Time"
    EXPIRY_DROPDOWN        = (By.CSS_SELECTOR, '[data-testid="trade-dropdown-expiry"]')

    # Stop Loss (common across all order types)
    STOPLOSS_INPUT        = (By.CSS_SELECTOR, '[data-testid="trade-input-stoploss-price"]')

    # Take Profit (common across all order types)
    TAKEPROFIT_INPUT      = (By.CSS_SELECTOR, '[data-testid="trade-input-takeprofit-price"]')

    # Open Trade button
    OPEN_TRADE_BUTTON     = (By.CSS_SELECTOR, '[data-testid="trade-button-order"]')
