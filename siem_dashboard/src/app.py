import argparse
import sys
from siem_dashboard.src.report import analyze_logs, print_report

SAMPLE_LOGS = [
    "2026-07-25 08:00:00 SRC_IP=192.168.1.10 DST_IP=10.0.0.1 ACTION=ALLOW",
    "2026-07-25 08:01:03 SRC_IP=185.220.101.1 DST_IP=10.0.0.5 ACTION=BLOCK REASON=PORT_SCAN",
    "2026-07-25 08:02:15 SRC_IP=203.0.113.5 DST_IP=10.0.0.2 ACTION=BLOCK REASON=ABUSEIPDB_HIGH_SCORE",
    "2026-07-25 08:03:00 SRC_IP=192.168.1.20 DST_IP=10.0.0.3 ACTION=ALLOW",
    "2026-07-25 08:04:22 SRC_IP=45.33.32.156 DST_IP=10.0.0.1 ACTION=BLOCK REASON=BRUTE_FORCE",
    "2026-07-25 08:05:01 SRC_IP=10.0.0.10 DST_IP=8.8.8.8 ACTION=ALLOW",
]


def main():
    parser = argparse.ArgumentParser(description="SIEM Log Analyzer & Reporter")
    parser.add_argument("--file", help="Path to log file (one log per line)")
    parser.add_argument("--verbose", action="store_true", help="Show all events")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file) as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: file '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        lines = SAMPLE_LOGS

    stats = analyze_logs(lines)
    print_report(stats)

    if args.verbose:
        print("\n=== All Events ===")
        for line in lines:
            print(line.strip())


if __name__ == "__main__":
    main()
