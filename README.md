# Freelance Portfolio – Febriyansyah

IT security leader (15+ yrs, banking) and Master's student in Informatics Engineering. Focused on ML for cybersecurity & finance.

## Projects

### Cyber Security

| Project | Description | Tech |
|---|---|---|
| `cyber_ml/` | Log analysis, threat scoring, AbuseIPDB API integration | Python |
| `siem-dashboard/` | SIEM log monitoring, event parsing, threat scoring | Python |
| `vulnerability-scanner/` | Port scanner with service detection & CVE reporting | Python |

### Machine Learning & Finance

| Project | Description | Tech |
|---|---|---|
| `fraud-detection/` | ML-based banking fraud detection + FastAPI | sklearn, FastAPI |
| `stock_ml/` | Stock signal generator + Yahoo Finance API | yfinance |
| `phishing-detector/` | URL phishing classifier (ML) | sklearn |

## Setup

```bash
pip install -r requirements.txt
```

## Test

```bash
pytest cyber_ml/tests/ stock_ml/tests/ fraud-detection/tests/ siem-dashboard/tests/ vulnerability-scanner/tests/ phishing-detector/tests/ -v
```

## Usage Quick Start

```bash
# AbuseIPDB check
python -m cyber_ml.abuseipdb_client 8.8.8.8 --api-key YOUR_KEY

# Stock signal
python -m stock_ml.yahoo_finance AAPL --period 1mo

# Fraud detection API
python -m fraud_detection.src.train
uvicorn fraud_detection.src.api:app

# SIEM report
python -m siem_dashboard.src.app

# Port scanner
python -m vulnerability_scanner.src.scanner --target scanme.nmap.org

# Phishing detector
python -m phishing_detector.src.classify --url "http://suspicious-login.com"
```

Contact: febriyansyah.research@gmail.com
