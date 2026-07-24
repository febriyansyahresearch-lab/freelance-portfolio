#!/bin/bash
set -e

echo "=== Building Docker image ==="
docker build -t freelance-portfolio .

echo "=== Running all tests ==="
docker run --rm freelance-portfolio python -m pytest \
  cyber_ml/tests/ stock_ml/tests/ \
  fraud-detection/tests/ siem-dashboard/tests/ \
  vulnerability-scanner/tests/ phishing-detector/tests/ \
  -v

echo "=== Done ==="
