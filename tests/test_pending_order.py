from page.trade_page import TradePage


def test_edit_pending_order(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    page.click_pending_orders_tab()
    form = page.edit_pending_order(trade_data["order_id"])
    form.enter_price(trade_data["edit_price"])
    form.select_expiry(trade_data["expiry_specified_date_and_time"])
    form.enter_expiry_date(trade_data["edit_expiry_date"])
    form.enter_expiry_time(trade_data["edit_expiry_time"])
    form.select_fill_policy(trade_data["fill_policy_limit_stop"])
    page.enter_stoploss_points(trade_data["edit_stoploss_points"])
    page.enter_takeprofit_points(trade_data["edit_takeprofit_points"])
    print(1)
