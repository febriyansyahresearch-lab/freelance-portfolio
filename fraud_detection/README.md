# Fraud Detection — ML-Based Transaction Fraud Classification

**Domain:** Banking Security, Financial Fraud Detection  
**Practitioner Level:** IT Security Leader (15+ yrs, Banking)  

## Problem Statement

Banking fraud detection must identify fraudulent transactions in real-time from highly imbalanced data (1:10,000 legitimate-to-fraud ratio). Traditional rule-based systems fail against adaptive fraud patterns.

## Methodology

1. **Synthetic Data Generation**: 2,000 transactions with 10 features (amount, time, merchant category, location distance, etc.)
2. **Class Imbalance Handling**: `class_weight="balanced"` in RandomForest
3. **Model Training**: RandomForest (100 estimators) with stratified 80/20 split
4. **Evaluation**: ROC-AUC + precision/recall per class
5. **Deployment**: FastAPI REST API with pre-trained model

## Key Concepts

- Imbalanced classification techniques
- Ensemble methods for robust detection
- API-first design for real-time scoring

## References

- Bhattacharyya et al. (2011). Data mining for credit card fraud: A comparative study. *DSS* 50(3).
- Phua et al. (2010). A comprehensive survey of data mining-based fraud detection.

## Usage

```bash
python -m fraud_detection.src.train
uvicorn fraud_detection.src.api:app
```
