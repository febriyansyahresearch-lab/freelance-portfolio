import pytest
from stock_ml.yahoo_finance import simple_signal


def test_simple_signal_buy():
    prices = [100, 102, 105]
    assert simple_signal(prices, threshold=1.0) == "BUY"


def test_simple_signal_sell():
    prices = [105, 102, 98]
    assert simple_signal(prices, threshold=1.0) == "SELL"


def test_simple_signal_hold():
    prices = [100, 100.5, 100.3]
    assert simple_signal(prices, threshold=1.0) == "HOLD"


def test_simple_signal_insufficient_data():
    assert simple_signal([100], threshold=1.0) == "HOLD"
    assert simple_signal([], threshold=1.0) == "HOLD"


def test_simple_signal_custom_threshold():
    prices = [100, 100.5]
    assert simple_signal(prices, threshold=2.0) == "HOLD"
    assert simple_signal(prices, threshold=0.3) == "BUY"
