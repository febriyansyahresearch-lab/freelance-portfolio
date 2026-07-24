import argparse
import sys

try:
    import yfinance as yf
except ImportError:
    yf = None


def fetch_prices(ticker: str, period: str = "5d") -> list[float]:
    if yf is None:
        print("Error: yfinance not installed. Run: pip install yfinance", file=sys.stderr)
        sys.exit(1)
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    if hist.empty:
        return []
    return hist["Close"].tolist()


def simple_signal(prices: list[float], threshold: float = 1.0) -> str:
    if len(prices) < 2:
        return "HOLD"
    last = prices[-1]
    prev = prices[-2]
    change = (last - prev) / prev * 100
    if change >= threshold:
        return "BUY"
    elif change <= -threshold:
        return "SELL"
    return "HOLD"


def main():
    parser = argparse.ArgumentParser(description="Stock signal using Yahoo Finance data")
    parser.add_argument("ticker", nargs="?", default="AAPL", help="Stock ticker symbol (default: AAPL)")
    parser.add_argument("--period", default="5d", help="Period to fetch (default: 5d)")
    parser.add_argument("--threshold", type=float, default=1.0, help="Change threshold %")
    parser.add_argument("--prices", nargs="*", type=float, help="Manual price list (bypasses yfinance)")
    args = parser.parse_args()

    if args.prices:
        prices = args.prices
    else:
        prices = fetch_prices(args.ticker, args.period)
        if not prices:
            print(f"No price data found for {args.ticker}", file=sys.stderr)
            sys.exit(1)
        print(f"Fetched {len(prices)} prices for {args.ticker}")

    sig = simple_signal(prices, args.threshold)
    print(f"Latest price: {prices[-1]:.2f}" if isinstance(prices[-1], float) else f"Latest price: {prices[-1]}")
    print(f"Signal: {sig}")


if __name__ == "__main__":
    main()
