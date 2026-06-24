import yfinance as yf

from src.models.enums import SignalVote
from src.signals.base import SignalResult


def compute_vix_regime() -> SignalResult:
    vix = yf.download("^VIX", period="1mo", auto_adjust=True, progress=False)
    if vix.empty:
        return SignalResult("vix_regime", SignalVote.NEUTRAL, 0.0, "sin datos")

    vix_close = vix["Close"].squeeze()
    vix_val = float(vix_close.iloc[-1])

    if vix_val < 15:
        return SignalResult("vix_regime", SignalVote.BULLISH, 1.0, f"VIX={vix_val:.1f} < 15")
    if vix_val < 25:
        return SignalResult("vix_regime", SignalVote.NEUTRAL, 1.0, f"VIX={vix_val:.1f} (15-25)")
    if vix_val < 30:
        return SignalResult("vix_regime", SignalVote.BEARISH, 1.0, f"VIX={vix_val:.1f} (25-30)")
    return SignalResult("vix_regime", SignalVote.BEARISH, 1.0, f"VIX={vix_val:.1f} > 30")
