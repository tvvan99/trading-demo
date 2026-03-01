from page.trade_page import TradePage, MarketOrderForm


def test_market_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    form = page.select_order_type("Market")

    form.enter_volume(trade_data["volume"])
    form.select_fill_policy(MarketOrderForm.FILL_OR_KILL)
    page.enter_stoploss(trade_data["stoploss"])
    page.enter_takeprofit(trade_data["takeprofit"])

    assert form.get_volume_value() == trade_data["volume"]
    assert page.get_stoploss_value() == trade_data["stoploss"]
    assert page.get_takeprofit_value() == trade_data["takeprofit"]


def test_limit_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    form = page.select_order_type("Limit")

    form.enter_price(trade_data["limit_price"])
    form.enter_volume(trade_data["volume"])
    form.select_fill_policy()
    page.enter_stoploss(trade_data["stoploss"])
    page.enter_takeprofit(trade_data["takeprofit"])

    assert form.get_price_value() == trade_data["limit_price"]
    assert form.get_volume_value() == trade_data["volume"]
    assert page.get_stoploss_value() == trade_data["stoploss"]
    assert page.get_takeprofit_value() == trade_data["takeprofit"]


def test_stop_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    form = page.select_order_type("Stop")

    form.enter_price(trade_data["stop_price"])
    form.enter_volume(trade_data["volume"])
    form.select_fill_policy()
    page.enter_stoploss(trade_data["stoploss"])
    page.enter_takeprofit(trade_data["takeprofit"])

    assert form.get_price_value() == trade_data["stop_price"]
    assert form.get_volume_value() == trade_data["volume"]
    assert page.get_stoploss_value() == trade_data["stoploss"]
    assert page.get_takeprofit_value() == trade_data["takeprofit"]


def test_enter_stoploss(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    page.enter_stoploss(trade_data["stoploss"])
    assert page.get_stoploss_value() == trade_data["stoploss"]
