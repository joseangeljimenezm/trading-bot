import yfinance as yf

from src.models.enums import SignalVote
from src.signals.base import SignalResult

LOOKBACK = 252


def compute_dual_momentum() -> SignalResult:
    spy = yf.download("SPY", period="1y", auto_adjust=True, progress=False)
    bil = yf.download("BIL", period="1y", auto_adjust=True, progress=False)
    vix = yf.download("^VIX", period="1mo", auto_adjust=True, progress=False)

    if spy.empty or bil.empty:
        return SignalResult("dual_momentum", SignalVote.NEUTRAL, 0.0, "sin datos")

    spy_close = spy["Close"].squeeze()
    bil_close = bil["Close"].squeeze()
    spy_ret = (spy_close.iloc[-1] / spy_close.iloc[0]) - 1
    bil_ret = (bil_close.iloc[-1] / bil_close.iloc[0]) - 1

    # Filtro VIX: si VIX > 25 → RISK OFF
    if not vix.empty:
        vix_close = vix["Close"].squeeze()
        vix_val = float(vix_close.iloc[-1])
    else:
        vix_val = 0

    if vix_val > 25:
        return SignalResult("dual_momentum", SignalVote.BEARISH, 1.0, f"VIX={vix_val:.1f} > 25")

    # SPY 12m > BIL 12m → RISK ON
    if spy_ret > bil_ret:
        return SignalResult("dual_momentum", SignalVote.BULLISH, 1.0, f"SPY {spy_ret:.1%} > BIL {bil_ret:.1%}")

    return SignalResult("dual_momentum", SignalVote.BEARISH, 1.0, f"SPY {spy_ret:.1%} < BIL {bil_ret:.1%}")
