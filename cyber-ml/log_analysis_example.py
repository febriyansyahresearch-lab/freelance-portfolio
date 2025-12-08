# log_analysis_example.py
# Simple demo: log parsing & basic threat scoring

sample_logs = [
    "2025-12-01 10:00:00 SRC_IP=192.168.1.10 ACTION=ALLOW",
    "2025-12-01 10:01:03 SRC_IP=185.220.101.1 ACTION=BLOCK REASON=ABUSEIPDB_HIGH_SCORE",
    "2025-12-01 10:02:15 SRC_IP=203.0.113.5 ACTION=BLOCK REASON=PORT_SCAN",
]

def score_log(line: str) -> int:
    line_up = line.upper()
    if "ABUSEIPDB_HIGH_SCORE" in line_up:
        return 90
    if "PORT_SCAN" in line_up:
        return 70
    if "BLOCK" in line_up:
        return 50
    return 10

if __name__ == "__main__":
    print("Simple log analysis demo (security-focused signal)")
    for log in sample_logs:
        score = score_log(log)
        print(f"{log} => threat_score={score}")
