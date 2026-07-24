# Phishing Detector — ML-Based URL Classification

**Domain:** Cybersecurity, Anti-Phishing  
**Practitioner Level:** IT Security Leader (15+ yrs, Banking)  

## Problem Statement

Phishing URLs bypass blocklists through rapid domain generation and URL obfuscation. ML-based URL classifiers detect malicious intent from structural features alone, without requiring page content analysis.

## Methodology

1. **Feature Engineering**: Extract 10 URL structural features:
   - URL length, dot/hyphen/slash count, `@` presence
   - HTTPS usage, IP-as-hostname detection
   - Subdomain count, path length, special character count
2. **Classifier**: RandomForest with balanced class weighting
3. **Synthetic Data**: Generate legitimate + obfuscated phishing URLs
4. **Evaluation**: Precision, recall, F1-score on held-out test set

## Key Concepts

- Heuristic URL feature extraction
- Content-agnostic classification (no page download needed)
- Feature engineering for URL obfuscation patterns

## References

- Garera et al. (2007). A framework for detection and measurement of phishing attacks. *ACM WORM*.
- Ma et al. (2009). Beyond blacklists: learning to detect malicious Web sites from suspicious URLs. *KDD '09*.

## Usage

```bash
python -m phishing_detector.src.classify --url "http://suspicious-login.com"
```
