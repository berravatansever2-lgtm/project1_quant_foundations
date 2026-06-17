# Quant Foundations

A Python implementation of core quantitative finance concepts built from first principles. This is the first project in a series building toward systematic trading strategies and financial ML models.

## What This Project Covers

### 1. Geometric Brownian Motion Simulation
Simulates 100 stochastic stock price paths over 252 trading days using the GBM model — the same mathematical framework underlying Black-Scholes options pricing.

- Models daily returns as normally distributed with drift `μ = 0.0005` and volatility `σ = 0.01`
- Demonstrates how uncertainty compounds over time (the fan shape)
- Illustrates tail risk — the range of outcomes from ~$80 to ~$180 from the same starting point

### 2. Real Market Data Analysis
Pulls historical SPY (S&P 500 ETF) price data using `yfinance` and computes empirically grounded risk metrics.

- Computes daily log returns rather than simple returns
- Log returns are used because they are time-additive — simple returns compound asymmetrically and cannot be summed across periods

### 3. Risk Metrics
Computes the three most fundamental quantitative risk measures on real market data:

| Metric | Formula | What It Measures |
|--------|---------|-----------------|
| Annualised Return | `mean(log_returns) × 252` | Expected yearly gain |
| Annualised Volatility | `std(log_returns) × √252` | Yearly risk (scaled by √252 because volatility scales with square root of time) |
| Sharpe Ratio | `(Return - Risk Free Rate) / Volatility` | Risk-adjusted performance |

## Results

### 2022 (Rate Hike Year)
| Metric | Value |
|--------|-------|
| Annualised Return | 1.32% |
| Annualised Volatility | 19.54% |
| Sharpe Ratio | -0.086 |

SPY returned only 1.32% — below the 3% risk-free rate — meaning investors were not compensated for the risk they took. The Federal Reserve's aggressive rate hikes drove simultaneous declines in both equities and bonds.

### 2023 (Recovery Year)
| Metric | Value |
|--------|-------|
| Annualised Return | 23.96% |
| Annualised Volatility | 13.08% |
| Sharpe Ratio | 1.60 |

A strong recovery year with a Sharpe ratio of 1.60 — well above the 1.0 threshold considered good risk-adjusted performance.

## Key Concepts Demonstrated

**Why log returns?** A 10% gain followed by a 10% loss on simple returns leaves you at $99, not $100. Log returns are symmetric and additive across time — essential for multi-period analysis.

**Why √252 for annualisation?** Volatility scales with the square root of time (a property of random walks), not linearly. Daily volatility × √252 gives annualised volatility.

**Why Sharpe ratio over raw return?** A strategy returning 15% with 40% volatility is worse risk-adjusted than one returning 12% with 5% volatility. Sharpe ratio makes this comparison possible.

**Volatility clustering** — the 2022 SPY return chart shows higher volatility concentrated around Fed announcement periods, an empirical phenomenon modelled by GARCH processes.

## Installation

```bash
pip install numpy pandas yfinance matplotlib
```

## Usage

```bash
python quant_foundations.py
```

Outputs:
- `gbm_simulation.png` — 100 simulated GBM price paths
- Printed risk metrics for SPY 2022–2024

## Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| numpy | ≥1.24 | Vectorised numerical computation |
| pandas | ≥2.0 | Financial time series manipulation |
| yfinance | ≥0.2 | Market data download |
| matplotlib | ≥3.7 | Visualisation |

## Next Steps for the curious!

- [ ] Moving average crossover backtest
- [ ] Black-Scholes options pricer
- [ ] Multi-asset correlation matrix
- [ ] Factor model (Fama-French 3-factor)
- [ ] ML-based return prediction pipeline
