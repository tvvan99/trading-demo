from page.trade_page import TradePage

def test_enter_stoploss(logged_in_driver, trade_data):
    page = TradePage(logged_in_driver)
    page.load()
    page.enter_stoploss(trade_data["stoploss"])
    assert page.get_stoploss_value() == trade_data["stoploss"]
    
