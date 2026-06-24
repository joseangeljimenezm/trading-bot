import yfinance as yf

from src.models.enums import SignalVote
from src.signals.base import SignalResult


def compute_usd_trend() -> SignalResult:
    uup = yf.download("UUP", period="1y", auto_adjust=True, progress=False)
    if uup.empty:
        return SignalResult("usd_trend", SignalVote.NEUTRAL, 0.0, "sin datos")

    close = uup["Close"].squeeze()
    current = float(close.iloc[-1])
    sma200 = float(close.tail(200).mean()) if len(close) >= 200 else float(close.mean())

    if current > sma200:
        return SignalResult("usd_trend", SignalVote.BULLISH, 1.0, f"USD={current:.2f} > SMA200={sma200:.2f} (fuerte)")
    return SignalResult("usd_trend", SignalVote.BEARISH, 1.0, f"USD={current:.2f} < SMA200={sma200:.2f} (débil)")
