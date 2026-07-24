import argparse
import json
import sys
import urllib.request
import urllib.error


ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip(ip_address: str, api_key: str, max_age: int = 90) -> dict:
    params = f"?ipAddress={ip_address}&maxAgeInDays={max_age}"
    req = urllib.request.Request(
        ABUSEIPDB_URL + params,
        headers={"Key": api_key, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"URL error: {e.reason}"}


def format_result(data: dict) -> str:
    if "error" in data:
        return f"Error: {data['error']}"
    d = data.get("data", {})
    return (
        f"IP: {d.get('ipAddress', 'N/A')}\n"
        f"Abuse Confidence Score: {d.get('abuseConfidenceScore', 0)}%\n"
        f"Country: {d.get('countryCode', 'N/A')}\n"
        f"Domain: {d.get('domain', 'N/A')}\n"
        f"Total Reports: {d.get('totalReports', 0)}\n"
        f"ISP: {d.get('isp', 'N/A')}"
    )


def main():
    parser = argparse.ArgumentParser(description="AbuseIPDB IP reputation checker")
    parser.add_argument("ip", help="IP address to check")
    parser.add_argument("--api-key", help="AbuseIPDB API key (or set ABUSEIPDB_API_KEY env var)")
    parser.add_argument("--max-age", type=int, default=90, help="Max age of reports in days (default: 90)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    api_key = args.api_key
    if not api_key:
        print("Error: API key required via --api-key or ABUSEIPDB_API_KEY env var", file=sys.stderr)
        sys.exit(1)

    result = check_ip(args.ip, api_key, args.max_age)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_result(result))


if __name__ == "__main__":
    main()
