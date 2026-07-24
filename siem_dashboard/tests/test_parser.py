import pytest
from siem_dashboard.src.parser import parse_log, score_event


def test_parse_valid_log():
    line = "2026-07-25 08:00:00 SRC_IP=192.168.1.1 DST_IP=10.0.0.1 ACTION=ALLOW"
    result = parse_log(line)
    assert result is not None
    assert result["src_ip"] == "192.168.1.1"
    assert result["action"] == "ALLOW"


def test_parse_log_with_reason():
    line = "2026-07-25 08:00:00 SRC_IP=1.2.3.4 ACTION=BLOCK REASON=PORT_SCAN"
    result = parse_log(line)
    assert result["reason"] == "PORT_SCAN"


def test_parse_invalid_log():
    assert parse_log("invalid log") is None


def test_score_event():
    ev = {"reason": "PORT_SCAN"}
    assert score_event(ev) == 70


def test_score_event_default():
    ev = {"action": "ALLOW"}
    assert score_event(ev) == 5
