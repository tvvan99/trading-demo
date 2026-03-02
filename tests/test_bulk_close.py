from page.trade_page import TradePage

BULK_CLOSE_ALL = "All Positions"


def _open_market_trade(driver, trade_data):
    """Helper: open one market trade using DEFAULT_ORDER_TYPE and confirm it."""
    page = TradePage(driver)
    form = page.select_order_type()

    form.enter_volume(trade_data["volume"])
    form.select_fill_policy(trade_data["fill_policy_market"])
    page.enter_stoploss_points(trade_data["stoploss_points"])
    page.enter_takeprofit_points(trade_data["takeprofit_points"])

    page.click_open_trade()
    page.confirm_trade()


def test_bulk_close_all_positions(logged_in_driver, trade_data):
    _open_market_trade(logged_in_driver, trade_data)
    _open_market_trade(logged_in_driver, trade_data)

    page = TradePage(logged_in_driver)
    page.bulk_close_select_option(BULK_CLOSE_ALL)
    page.bulk_close_confirm(BULK_CLOSE_ALL)
