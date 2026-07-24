#!/bin/bash
set -e

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Training fraud detection model ==="
python -m fraud_detection.src.train

echo "=== Training phishing detector model ==="
python -m phishing_detector.src.train

echo "=== Running tests ==="
python -m pytest cyber_ml/tests/ stock_ml/tests/ fraud_detection/tests/ siem_dashboard/tests/ vulnerability_scanner/tests/ phishing_detector/tests/ -v

echo "=== Setup complete ==="
