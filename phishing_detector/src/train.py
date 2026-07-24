import joblib
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from phishing_detector.src.features import feature_vector

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

SAMPLE_URLS = [
    ("https://google.com", 0),
    ("https://github.com", 0),
    ("https://login.secure-bank.com", 1),
    ("http://192.168.1.1/login", 1),
    ("https://www.paypal.com", 0),
    ("http://free-money.click/claim.php", 1),
    ("https://mail.google.com", 0),
    ("http://bit.ly/3xyzabc", 1),
    ("https://www.linkedin.com", 0),
    ("http://secure-login.xyz/verify", 1),
    ("https://stackoverflow.com", 0),
    ("http://refund-account.info/update", 1),
    ("https://www.amazon.com", 0),
    ("http://support-apple.xyz/help", 1),
    ("https://drive.google.com", 0),
    ("https://www.facebook.com", 0),
    ("http://verify-paypal.account-security.com", 1),
    ("https://twitter.com", 0),
    ("http://free-iphone.click/win.php", 1),
    ("https://www.microsoft.com", 0),
    ("http://bank-secure-login.xyz/auth", 1),
    ("https://www.instagram.com", 0),
    ("http://account-verify.xyz/reset", 1),
    ("https://www.wikipedia.org", 0),
    ("http://win-prize.click/claim", 1),
    ("https://www.netflix.com", 0),
    ("http://secure-update.xyz/install", 1),
    ("https://www.reddit.com", 0),
    ("http://tax-refund.xyz/claim", 1),
    ("https://www.whatsapp.com", 0),
]


def train():
    X = np.array([feature_vector(url) for url, _ in SAMPLE_URLS])
    y = np.array([label for _, label in SAMPLE_URLS])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=["Legitimate", "Phishing"]))

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, os.path.join(MODEL_DIR, "phishing_model.joblib"))
    print("Model saved to models/phishing_model.joblib")


if __name__ == "__main__":
    train()
