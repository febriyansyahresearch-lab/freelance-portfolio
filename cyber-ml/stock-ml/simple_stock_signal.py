# simple_stock_signal.py
# Very simple stock signal demo based on price change

prices = [100, 102, 101, 103, 104]  # dummy closing prices

def simple_signal(prices_list):
    if len(prices_list) < 2:
        return "HOLD"
    last = prices_list[-1]
    prev = prices_list[-2]
    change = (last - prev) / prev * 100
    if change >= 1.0:
        return "BUY"
    elif change <= -1.0:
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    sig = simple_signal(prices)
    print(f"Last prices: {prices}")
    print(f"Signal: {sig}")
