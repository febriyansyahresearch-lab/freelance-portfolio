import pytest
from cyber_ml.abuseipdb_client import format_result


def test_format_result_with_valid_data():
    data = {
        "data": {
            "ipAddress": "8.8.8.8",
            "abuseConfidenceScore": 0,
            "countryCode": "US",
            "domain": "dns.google",
            "totalReports": 0,
            "isp": "Google LLC",
        }
    }
    result = format_result(data)
    assert "8.8.8.8" in result
    assert "0%" in result


def test_format_result_with_error():
    data = {"error": "Not found"}
    result = format_result(data)
    assert "Error" in result
    assert "Not found" in result


def test_format_result_empty_data():
    data = {}
    result = format_result(data)
    assert "N/A" in result
