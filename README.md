# Freelance Portfolio – Febriyansyah

IT security leader (15+ yrs, banking) and Master's student in Informatics Engineering. Focused on ML for cybersecurity & stocks.

## Cyber ML
- `log_analysis_example.py` — Simple log parsing & threat scoring
- `abuseipdb_client.py` — AbuseIPDB API integration (check IP reputation)
- `tests/` — Unit tests

## Stock ML
- `simple_stock_signal.py` — Simple stock signal (BUY/SELL/HOLD) based on price change
- `yahoo_finance.py` — Real stock data via Yahoo Finance API
- `tests/` — Unit tests

## Setup
```bash
pip install -r requirements.txt
```

## Usage
```bash
# AbuseIPDB
python -m cyber_ml.abuseipdb_client 8.8.8.8 --api-key YOUR_KEY

# Yahoo Finance
python -m stock_ml.yahoo_finance AAPL --period 1mo

# Run tests
pytest
```

Contact: febriyansyah.research@gmail.com
