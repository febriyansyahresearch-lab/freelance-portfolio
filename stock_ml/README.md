# Stock ML — Technical Analysis Signal Generator

**Domain:** Quantitative Finance, FinTech  
**Practitioner Level:** IT Security Leader (15+ yrs, Banking)  

## Problem Statement

Algorithmic trading strategies require automated signal generation from price data. Simple momentum-based indicators (percentage price change vs. threshold) provide baseline buy/sell/hold signals for equities.

## Methodology

1. **Data Acquisition**: Yahoo Finance API via `yfinance` library
2. **Signal Generation**: Simple momentum strategy:
   - $Signal = ((P_{t} - P_{t-1}) / P_{t-1}) \times 100$
   - BUY if change $\geq$ threshold (default: 1%)
   - SELL if change $\leq$ -threshold
   - HOLD otherwise
3. **Flexibility**: Configurable ticker, period, threshold via CLI

## Key Concepts

- Momentum-based technical analysis
- API-based market data acquisition
- CLI-first tool design

## References

- Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. NYIF.
- Lo, A. W., Mamaysky, H., & Wang, J. (2000). Foundations of Technical Analysis. *Journal of Finance*, 55(4).

## Usage

```bash
python -m stock_ml.yahoo_finance AAPL --period 1mo
python -m stock_ml.simple_stock_signal --prices 100 102 101 103 104
```
