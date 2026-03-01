from page.trade_page import TradePage


def test_market_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    form = page.select_order_type()  # defaults to DEFAULT_ORDER_TYPE from .env

    form.enter_volume(trade_data["volume"])
    form.select_fill_policy(trade_data["fill_policy_market"])
    page.enter_stoploss(trade_data["stoploss"])
    page.enter_takeprofit(trade_data["takeprofit"])

    assert form.get_volume_value() == trade_data["volume"]
    assert page.get_stoploss_value() == trade_data["stoploss"]
    assert page.get_takeprofit_value() == trade_data["takeprofit"]

    page.click_open_trade()


def test_limit_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    form = page.select_order_type(trade_data["order_type_limit"])

    form.enter_price(trade_data["limit_price"])
    form.enter_volume(trade_data["volume"])
    form.select_fill_policy(trade_data["fill_policy_limit_stop"])
    page.enter_stoploss(trade_data["stoploss"])
    page.enter_takeprofit(trade_data["takeprofit"])

    assert form.get_price_value() == trade_data["limit_price"]
    assert form.get_volume_value() == trade_data["volume"]
    assert page.get_stoploss_value() == trade_data["stoploss"]
    assert page.get_takeprofit_value() == trade_data["takeprofit"]

    page.click_open_trade()


def test_stop_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    form = page.select_order_type(trade_data["order_type_stop"])

    form.enter_price(trade_data["stop_price"])
    form.enter_volume(trade_data["volume"])
    form.select_fill_policy(trade_data["fill_policy_limit_stop"])
    page.enter_stoploss(trade_data["stoploss"])
    page.enter_takeprofit(trade_data["takeprofit"])

    assert form.get_price_value() == trade_data["stop_price"]
    assert form.get_volume_value() == trade_data["volume"]
    assert page.get_stoploss_value() == trade_data["stoploss"]
    assert page.get_takeprofit_value() == trade_data["takeprofit"]

    page.click_open_trade()


