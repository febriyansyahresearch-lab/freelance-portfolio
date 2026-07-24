#!/bin/bash
set -e

echo "=== Building Docker image ==="
docker build -t freelance-portfolio .

echo "=== Running tests ==="
docker run --rm freelance-portfolio python -m pytest cyber_ml/tests/ stock_ml/tests/ -v

echo "=== Running AbuseIPDB example ==="
docker run --rm freelance-portfolio python -m cyber_ml.abuseipdb_client 8.8.8.8 --help

echo "=== Running Stock ML example ==="
docker run --rm freelance-portfolio python -m stock_ml.yahoo_finance --help

echo "=== Done ==="
