import pytest
from fraud_detection.src.data import generate_transactions


def test_generate_transactions_shape():
    df = generate_transactions(n=500)
    assert len(df) == 500
    assert "is_fraud" in df.columns


def test_fraud_ratio():
    df = generate_transactions(n=1000, fraud_ratio=0.1)
    ratio = df["is_fraud"].mean()
    assert 0.05 <= ratio <= 0.15


def test_columns_present():
    df = generate_transactions(n=100)
    expected = {"amount", "hour", "distance_km", "prev_failures", "is_international", "is_fraud"}
    assert expected.issubset(set(df.columns))
