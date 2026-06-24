import yfinance as yf

from src.models.enums import SignalVote
from src.signals.base import SignalResult


def compute_oil_shock() -> SignalResult:
    cl = yf.download("CL=F", period="2mo", auto_adjust=True, progress=False)
    if cl.empty:
        return SignalResult("oil_shock", SignalVote.NEUTRAL, 0.0, "sin datos")

    close = cl["Close"].squeeze()
    ret_30d = (close.iloc[-1] / close.iloc[-21]) - 1 if len(close) > 21 else (close.iloc[-1] / close.iloc[0]) - 1

    if ret_30d > 0.10:
        return SignalResult("oil_shock", SignalVote.BEARISH, 1.0, f"Oil +{ret_30d:.1%} en 30d (shock subida)")
    if ret_30d < -0.10:
        return SignalResult("oil_shock", SignalVote.BULLISH, 1.0, f"Oil {ret_30d:.1%} en 30d (shock bajada)")
    return SignalResult("oil_shock", SignalVote.NEUTRAL, 1.0, f"Oil {ret_30d:.1%} en 30d (normal)")
