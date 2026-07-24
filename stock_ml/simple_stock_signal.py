import argparse
import sys


DEFAULT_PRICES = [100, 102, 101, 103, 104]
DEFAULT_THRESHOLD = 1.0


def simple_signal(prices_list: list[float], threshold: float = DEFAULT_THRESHOLD) -> str:
    if len(prices_list) < 2:
        return "HOLD"
    last = prices_list[-1]
    prev = prices_list[-2]
    change = (last - prev) / prev * 100
    if change >= threshold:
        return "BUY"
    elif change <= -threshold:
        return "SELL"
    return "HOLD"


def main():
    parser = argparse.ArgumentParser(description="Simple stock signal based on price change")
    parser.add_argument("prices", nargs="*", type=float, help="Price history (space-separated)")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help=f"Change threshold %% (default: {DEFAULT_THRESHOLD})")
    parser.add_argument("--file", help="Path to CSV file with one price per line")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file) as f:
                prices = [float(line.strip()) for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: file '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
        except ValueError:
            print("Error: invalid price value in file", file=sys.stderr)
            sys.exit(1)
    elif args.prices:
        prices = args.prices
    else:
        prices = DEFAULT_PRICES

    sig = simple_signal(prices, args.threshold)
    print(f"Prices: {prices}")
    print(f"Signal: {sig}")


if __name__ == "__main__":
    main()
