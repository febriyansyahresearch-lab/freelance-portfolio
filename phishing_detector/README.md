# Phishing Detector

ML-based URL phishing detection classifier.

## Features
- URL feature extraction (length, special chars, domain age)
- ML classifier (RandomForest)
- Real-time prediction API
- Batch URL checking from file

## Usage
```bash
python -m phishing-detector.src.classify --url "http://suspicious-login.com"
```
