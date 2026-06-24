import requests
from datetime import datetime, timedelta

from src.models.enums import SignalVote
from src.signals.base import SignalResult
from src.config import FRED_API_KEY


def compute_liquidity() -> SignalResult:
    params = {
        "series_id": "WALCL",
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 30,
    }
    resp = requests.get("https://api.stlouisfed.org/fred/series/observations", params=params, timeout=10)
    resp.raise_for_status()
    obs = resp.json().get("observations", [])
    if len(obs) < 2:
        return SignalResult("liquidity", SignalVote.NEUTRAL, 0.0, "sin datos")

    values = []
    for o in obs:
        if o["value"] != ".":
            values.append(float(o["value"]))
    if len(values) < 2:
        return SignalResult("liquidity", SignalVote.NEUTRAL, 0.0, "sin datos")

    trend = (values[0] / values[-1]) - 1
    if trend > 0.01:
        return SignalResult("liquidity", SignalVote.BULLISH, 1.0, f"Fed balance +{trend:.2%} (expansión)")
    if trend < -0.01:
        return SignalResult("liquidity", SignalVote.BEARISH, 1.0, f"Fed balance {trend:.2%} (contracción)")
    return SignalResult("liquidity", SignalVote.NEUTRAL, 1.0, f"Fed balance {trend:.2%} (estable)")
