# Freelance Portfolio — Febriyansyah

**Febriyansyah** — MTI, IT Security Leader (15+ yrs, Banking)

Applied machine learning and cybersecurity engineering portfolio demonstrating MTI-level competency across fraud detection, threat intelligence, SIEM automation, vulnerability management, and quantitative finance.

## Projects

### Cybersecurity Engineering

| Project | Description | Methodology | References |
|---|---|---|---|
| `cyber_ml/` | Log analysis, threat scoring, AbuseIPDB API enrichment | Rule-based scoring, threat intel integration | AbuseIPDB, MITRE ATT&CK |
| `siem_dashboard/` | Regex log parser, threat report generator | Pattern matching, weighted threat scoring | NIST SP 800-92, Chuvakin (2013) |
| `vulnerability_scanner/` | TCP port scanner with CVE correlation | TCP connect scan, service fingerprinting | NVD, Lyon (2009) |

### Machine Learning & Finance

| Project | Description | Methodology | References |
|---|---|---|---|
| `fraud_detection/` | ML-based banking fraud detection + FastAPI | RandomForest, class-weight balancing | Bhattacharyya (2011), Phua (2010) |
| `phishing_detector/` | URL phishing classifier (10 feature extraction) | Heuristic feature engineering, RF | Garera (2007), Ma (2009) |
| `stock_ml/` | Stock signal generator + Yahoo Finance API | Momentum-based technical analysis | Murphy (1999), Lo (2000) |

## Setup

```bash
pip install -r requirements.txt
```

## Test

```bash
pytest cyber_ml/tests/ stock_ml/tests/ fraud_detection/tests/ siem_dashboard/tests/ vulnerability_scanner/tests/ phishing_detector/tests/ -v
```

## Usage Quick Start

```bash
# Fraud detection API
python -m fraud_detection.src.train
uvicorn fraud_detection.src.api:app

# Phishing URL check
python -m phishing_detector.src.classify --url "http://suspicious-login.com"

# Port scanner
python -m vulnerability_scanner.src.scanner --target scanme.nmap.org

# SIEM report
python -m siem_dashboard.src.app --file sample.log

# AbuseIPDB check
python -m cyber_ml.abuseipdb_client 8.8.8.8 --api-key YOUR_KEY

# Stock signal
python -m stock_ml.yahoo_finance AAPL --period 1mo
```

## Research & References

See `references/methodology.md` for detailed academic citations.

Contact: febriyansyah.research@gmail.com
