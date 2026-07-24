import numpy as np
import pandas as pd


def generate_transactions(n: int = 1000, fraud_ratio: float = 0.05, random_state: int = 42) -> pd.DataFrame:
    np.random.seed(random_state)
    n_fraud = int(n * fraud_ratio)
    n_normal = n - n_fraud

    normal = pd.DataFrame({
        "amount": np.random.exponential(scale=500, size=n_normal).clip(1, 50000),
        "hour": np.random.randint(0, 24, n_normal),
        "distance_km": np.random.exponential(scale=50, size=n_normal).clip(1, 1000),
        "prev_failures": np.random.poisson(lam=0.2, size=n_normal),
        "is_international": np.random.choice([0, 1], n_normal, p=[0.8, 0.2]),
        "is_fraud": 0,
    })

    fraud = pd.DataFrame({
        "amount": np.random.exponential(scale=5000, size=n_fraud).clip(500, 100000),
        "hour": np.random.randint(0, 24, n_fraud),
        "distance_km": np.random.exponential(scale=500, size=n_fraud).clip(100, 10000),
        "prev_failures": np.random.poisson(lam=3, size=n_fraud),
        "is_international": np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
        "is_fraud": 1,
    })

    df = pd.concat([normal, fraud], ignore_index=True)
    return df.sample(frac=1).reset_index(drop=True)
