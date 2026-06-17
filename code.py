
# Built: June 2026
# Concepts: GBM simulation, log returns, 
#           volatility, Sharpe ratio

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# ── 1. GBM Simulation ──────────────────────
plt.figure(figsize=(10, 5))
for i in range(100):
    returns = np.random.normal(0.0005, 0.01, 252)
    prices = [100]
    for r in returns:
        prices.append(prices[-1] * (1 + r))
    plt.plot(prices, alpha=0.3)
plt.title("100 GBM Simulated Paths")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.grid(True)
plt.savefig("gbm_simulation.png")
plt.show()

# ── 2. Real SPY Data ───────────────────────
spy = yf.download("SPY", start="2022-01-01", 
                  end="2024-01-01")
log_returns = np.log(
    spy["Close"] / spy["Close"].shift(1)
).dropna()

# ── 3. Risk Metrics ────────────────────────
risk_free = 0.03
ann_return = log_returns.mean() * 252
ann_vol = log_returns.std() * np.sqrt(252)
sharpe = (ann_return - risk_free) / ann_vol

print(f"Annualised Return: {ann_return.values[0]:.2%}")
print(f"Annualised Volatility: {ann_vol.values[0]:.2%}")
print(f"Sharpe Ratio: {sharpe.values[0]:.4f}")
