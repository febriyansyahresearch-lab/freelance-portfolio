from collections import Counter
from siem_dashboard.src.parser import parse_log, score_event


def analyze_logs(lines: list[str]) -> dict:
    events = []
    scores = []
    for line in lines:
        ev = parse_log(line)
        if ev:
            ev["score"] = score_event(ev)
            events.append(ev)
            scores.append(ev["score"])

    src_ips = Counter(e["src_ip"] for e in events)
    actions = Counter(e["action"] for e in events)

    return {
        "total_events": len(events),
        "avg_score": sum(scores) / len(scores) if scores else 0,
        "max_score": max(scores) if scores else 0,
        "top_src_ips": src_ips.most_common(5),
        "actions": dict(actions),
        "high_risk": [e for e in events if e["score"] >= 70],
    }


def print_report(stats: dict):
    print("=== SIEM Report ===")
    print(f"Total Events: {stats['total_events']}")
    print(f"Avg Threat Score: {stats['avg_score']:.1f}")
    print(f"Max Threat Score: {stats['max_score']}")
    print(f"\nTop Source IPs: {stats['top_src_ips']}")
    print(f"Actions: {stats['actions']}")
    if stats["high_risk"]:
        print(f"\nHigh Risk Events ({len(stats['high_risk'])}):")
        for e in stats["high_risk"]:
            print(f"  [{e['score']}] {e['src_ip']} -> {e['action']}: {e['reason']}")
