import re
from urllib.parse import urlparse


def extract_features(url: str) -> dict:
    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    return {
        "url_length": len(url),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_slashes": url.count("/"),
        "num_at": url.count("@"),
        "has_https": 1 if parsed.scheme == "https" else 0,
        "has_ip": 1 if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", hostname) else 0,
        "num_subdomains": len(hostname.split(".")) - 2 if hostname.count(".") >= 2 else 0,
        "path_length": len(parsed.path),
        "num_special_chars": sum(1 for c in url if c in "#?&%=;"),
    }


def feature_vector(url: str) -> list[float]:
    feats = extract_features(url)
    return list(feats.values())
