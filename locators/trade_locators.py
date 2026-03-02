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

    # Expiry date/time inputs (visible for "Specified Date" and "Specified Date and Time" only)
    EXPIRY_DATE_INPUT      = (By.CSS_SELECTOR, '[data-testid="trade-input-expiry-date"]')
    EXPIRY_TIME_INPUT      = (By.CSS_SELECTOR, '[data-testid="trade-input-expiry-time"]')

    # react-calendar navigation (shared by both date pickers)
    EXPIRY_CALENDAR_LABEL      = (By.CSS_SELECTOR, '.react-calendar__navigation__label')
    EXPIRY_CALENDAR_PREV_YEAR  = (By.CSS_SELECTOR, '.react-calendar__navigation__prev2-button')
    EXPIRY_CALENDAR_PREV_MONTH = (By.CSS_SELECTOR, '.react-calendar__navigation__prev-button')
    EXPIRY_CALENDAR_NEXT_MONTH = (By.CSS_SELECTOR, '.react-calendar__navigation__next-button')
    EXPIRY_CALENDAR_NEXT_YEAR  = (By.CSS_SELECTOR, '.react-calendar__navigation__next2-button')

    # Time picker — Hour/Minute custom dropdowns + OK button
    EXPIRY_TIME_HOUR_TRIGGER   = (By.XPATH, '//div[text()="Hour"]/following-sibling::div')
    EXPIRY_TIME_MINUTE_TRIGGER = (By.XPATH, '//div[text()="Minute"]/following-sibling::div')
    EXPIRY_TIME_OPTIONS        = (By.CSS_SELECTOR, '[data-testid="options"]')
    EXPIRY_TIME_OK             = (By.XPATH, '//button[normalize-space(text())="OK"]')
    EXPIRY_TIME_CLEAR          = (By.XPATH, '//button[normalize-space(text())="Clear"]')

    # Stop Loss (common across all order types)
    STOPLOSS_INPUT        = (By.CSS_SELECTOR, '[data-testid="trade-input-stoploss-price"]')
    STOPLOSS_POINTS_INPUT = (By.CSS_SELECTOR, '[data-testid="trade-input-stoploss-points"]')

    # Take Profit (common across all order types)
    TAKEPROFIT_INPUT        = (By.CSS_SELECTOR, '[data-testid="trade-input-takeprofit-price"]')
    TAKEPROFIT_POINTS_INPUT = (By.CSS_SELECTOR, '[data-testid="trade-input-takeprofit-points"]')

    # Open Trade button
    OPEN_TRADE_BUTTON     = (By.CSS_SELECTOR, '[data-testid="trade-button-order"]')

    # Trade confirmation dialog
    CONFIRM_BUTTON        = (By.CSS_SELECTOR, '[data-testid="trade-confirmation-button-confirm"]')
    CANCEL_BUTTON         = (By.CSS_SELECTOR, '[data-testid="trade-confirmation-button-close"]')

    # Bulk close dropdown
    BULK_CLOSE_DROPDOWN = (By.CSS_SELECTOR, '[data-testid="bulk-close"]')

    # Bulk close modals — All Positions
    BULK_CLOSE_CONFIRM_ALL    = (By.CSS_SELECTOR, '[data-testid="bulk-close-modal-button-submit-all"]')
    BULK_CLOSE_CANCEL_ALL     = (By.CSS_SELECTOR, '[data-testid="bulk-close-modal-button-cancel-all"]')

    # Bulk close modals — Profitable Positions
    BULK_CLOSE_CONFIRM_PROFIT = (By.CSS_SELECTOR, '[data-testid="bulk-close-modal-button-submit-profit"]')
    BULK_CLOSE_CANCEL_PROFIT  = (By.CSS_SELECTOR, '[data-testid="bulk-close-modal-button-cancel-profit"]')

    # Bulk close modals — Loss Positions
    BULK_CLOSE_CONFIRM_LOSS   = (By.CSS_SELECTOR, '[data-testid="bulk-close-modal-button-submit-loss"]')
    BULK_CLOSE_CANCEL_LOSS    = (By.CSS_SELECTOR, '[data-testid="bulk-close-modal-button-cancel-loss"]')
