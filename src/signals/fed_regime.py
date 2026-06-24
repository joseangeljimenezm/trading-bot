import requests
from datetime import datetime, timedelta

from src.models.enums import SignalVote
from src.signals.base import SignalResult
from src.config import FRED_API_KEY


def compute_fed_regime() -> SignalResult:
    params = {
        "series_id": "FEDFUNDS",
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 2,
    }
    resp = requests.get("https://api.stlouisfed.org/fred/series/observations", params=params, timeout=10)
    resp.raise_for_status()
    obs = resp.json().get("observations", [])
    if len(obs) < 2:
        return SignalResult("fed_regime", SignalVote.NEUTRAL, 0.0, "sin datos")

    rate = float(obs[0]["value"]) if obs[0]["value"] != "." else 0
    prev = float(obs[1]["value"]) if obs[1]["value"] != "." else 0
    trend = "subiendo" if rate > prev else "bajando"

    if rate <= 2:
        vote = SignalVote.BULLISH
    elif rate <= 5:
        vote = SignalVote.NEUTRAL
    else:
        vote = SignalVote.BEARISH

    return SignalResult("fed_regime", vote, 1.0, f"Fed rate={rate:.2f}% ({trend})")
