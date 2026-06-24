import yfinance as yf
import pandas as pd

from src.models.enums import SignalVote
from src.signals.base import SignalResult


def compute_canary() -> SignalResult:
    spy = yf.download("SPY", period="3mo", auto_adjust=True, progress=False)
    hyg = yf.download("HYG", period="3mo", auto_adjust=True, progress=False)
    if spy.empty or hyg.empty:
        return SignalResult("canary", SignalVote.NEUTRAL, 0.0, "sin datos")

    spy_ret = spy["Close"].squeeze().pct_change().dropna()
    hyg_ret = hyg["Close"].squeeze().pct_change().dropna()
    combined = pd.concat([spy_ret, hyg_ret], axis=1, join="inner").dropna()
    corr = combined.iloc[:, 0].rolling(20).corr(combined.iloc[:, 1])
    last_corr = float(corr.iloc[-1])

    if last_corr < 0.6:
        return SignalResult("canary", SignalVote.BEARISH, 1.0, f"corr SPY-HYG={last_corr:.2f} < 0.6")
    if last_corr > 0.8:
        return SignalResult("canary", SignalVote.BULLISH, 1.0, f"corr SPY-HYG={last_corr:.2f} > 0.8")
    return SignalResult("canary", SignalVote.NEUTRAL, 1.0, f"corr SPY-HYG={last_corr:.2f}")
