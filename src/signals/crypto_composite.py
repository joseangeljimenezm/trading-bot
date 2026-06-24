import yfinance as yf
import requests

from src.models.enums import SignalVote
from src.signals.base import SignalResult


def compute_crypto_composite() -> SignalResult:
    btc = yf.download("BTC-USD", period="1y", auto_adjust=True, progress=False)
    if btc.empty:
        return SignalResult("crypto_composite", SignalVote.NEUTRAL, 0.0, "sin datos")

    close = btc["Close"].squeeze()
    current = float(close.iloc[-1])
    sma200 = float(close.tail(200).mean()) if len(close) >= 200 else float(close.mean())
    btc_trend = current > sma200

    fear_greed = _fetch_fear_greed()
    is_extreme_fear = fear_greed < 25 if fear_greed else False

    bull_score = 0
    bear_score = 0
    if btc_trend:
        bull_score += 0.6
    else:
        bear_score += 0.6
    if is_extreme_fear:
        bull_score += 0.4
    elif fear_greed and fear_greed > 75:
        bear_score += 0.4

    if bull_score > bear_score:
        vote = SignalVote.BULLISH
    elif bear_score > bull_score:
        vote = SignalVote.BEARISH
    else:
        vote = SignalVote.NEUTRAL

    fg_str = f"FG={fear_greed}" if fear_greed else "FG=N/A"
    detail = f"BTC={current:,.0f}, SMA200={sma200:,.0f} ({'arriba' if btc_trend else 'abajo'}), {fg_str}"
    return SignalResult("crypto_composite", vote, 1.0, detail)


def _fetch_fear_greed() -> int | None:
    try:
        resp = requests.get("https://api.alternative.me/fng/?limit=1", timeout=10)
        return int(resp.json()["data"][0]["value"])
    except Exception:
        return None
