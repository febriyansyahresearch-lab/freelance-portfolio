import re
from datetime import datetime
from typing import Optional


LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"SRC_IP=(?P<src_ip>[\d.]+) ?"
    r"(?:DST_IP=(?P<dst_ip>[\d.]+) ?)?"
    r"ACTION=(?P<action>\w+)"
    r"(?: ?REASON=(?P<reason>.+))?$"
)


def parse_log(line: str) -> Optional[dict]:
    m = LOG_PATTERN.match(line.strip())
    if not m:
        return None
    return {
        "timestamp": m.group("timestamp"),
        "src_ip": m.group("src_ip"),
        "dst_ip": m.group("dst_ip") or "N/A",
        "action": m.group("action"),
        "reason": m.group("reason") or "",
    }


THREAT_SCORES = {
    "ABUSEIPDB_HIGH_SCORE": 90,
    "PORT_SCAN": 70,
    "BRUTE_FORCE": 85,
    "MALWARE": 95,
    "BLOCK": 50,
}


def score_event(event: dict) -> int:
    reason = event.get("reason", "").upper()
    for keyword, score in THREAT_SCORES.items():
        if keyword in reason:
            return score
    return 10 if event.get("action") == "BLOCK" else 5
