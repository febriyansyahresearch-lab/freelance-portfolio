import argparse
import sys


SAMPLE_LOGS = [
    "2025-12-01 10:00:00 SRC_IP=192.168.1.10 ACTION=ALLOW",
    "2025-12-01 10:01:03 SRC_IP=185.220.101.1 ACTION=BLOCK REASON=ABUSEIPDB_HIGH_SCORE",
    "2025-12-01 10:02:15 SRC_IP=203.0.113.5 ACTION=BLOCK REASON=PORT_SCAN",
]

THREAT_RULES = {
    "ABUSEIPDB_HIGH_SCORE": 90,
    "PORT_SCAN": 70,
    "BLOCK": 50,
}


def score_log(line: str) -> int:
    line_up = line.upper()
    for keyword, score in THREAT_RULES.items():
        if keyword in line_up:
            return score
    return 10


def analyze_logs(lines: list[str]) -> list[tuple[str, int]]:
    return [(line.strip(), score_log(line)) for line in lines]


def main():
    parser = argparse.ArgumentParser(description="Simple log analysis & threat scoring")
    parser.add_argument("file", nargs="?", help="Path to log file (optional)")
    parser.add_argument("--score-only", action="store_true", help="Print threat scores only")
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

    results = analyze_logs(lines)

    for line, score in results:
        if args.score_only:
            print(score)
        else:
            print(f"{line} => threat_score={score}")


if __name__ == "__main__":
    main()
