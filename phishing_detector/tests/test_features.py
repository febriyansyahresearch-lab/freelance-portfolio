import pytest
from phishing_detector.src.features import extract_features, feature_vector


def test_extract_features_normal_url():
    feats = extract_features("https://google.com")
    assert feats["has_https"] == 1
    assert feats["has_ip"] == 0
    assert feats["num_dots"] == 1


def test_extract_features_ip_url():
    feats = extract_features("http://192.168.1.1/login")
    assert feats["has_ip"] == 1
    assert feats["has_https"] == 0


def test_extract_features_suspicious():
    feats = extract_features("http://login.secure-bank.xyz/verify?token=abc")
    assert feats["num_subdomains"] >= 1
    assert feats["num_special_chars"] > 0


def test_feature_vector_length():
    vec = feature_vector("https://example.com")
    assert len(vec) == 10
    assert all(isinstance(v, (int, float)) for v in vec)
