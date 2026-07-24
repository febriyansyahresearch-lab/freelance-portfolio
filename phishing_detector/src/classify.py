import argparse
import joblib
import os
import sys
import numpy as np
from phishing_detector.src.features import feature_vector

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "phishing_model.joblib")


def load_model():
    if not os.path.exists(MODEL_PATH):
        print("Model not found. Run training first: python -m phishing_detector.src.train", file=sys.stderr)
        sys.exit(1)
    return joblib.load(MODEL_PATH)


def classify_url(url: str) -> dict:
    model = load_model()
    vec = np.array([feature_vector(url)])
    proba = model.predict_proba(vec)[0]
    pred = model.predict(vec)[0]
    return {
        "url": url,
        "prediction": "Phishing" if pred == 1 else "Legitimate",
        "confidence": round(float(max(proba)), 4),
    }


def main():
    parser = argparse.ArgumentParser(description="URL Phishing Detector")
    parser.add_argument("--url", help="Single URL to check")
    parser.add_argument("--file", help="File with URLs (one per line)")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            urls = [line.strip() for line in f if line.strip()]
        for url in urls:
            result = classify_url(url)
            print(f"[{result['prediction']}] {result['url']} (confidence: {result['confidence']:.2%})")
    elif args.url:
        result = classify_url(args.url)
        print(f"URL: {result['url']}")
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']:.2%}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
