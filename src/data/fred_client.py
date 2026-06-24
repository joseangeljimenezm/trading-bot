from datetime import datetime, timedelta

import pandas as pd
import requests

from src.config import FRED_API_KEY, TICKERS_FRED

BASE = "https://api.stlouisfed.org/fred/series/observations"


def fetch_series(series_id: str, days: int = 365 * 5) -> pd.DataFrame | None:
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d"),
        "sort_order": "desc",
    }
    resp = requests.get(BASE, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json().get("observations", [])
    if not data:
        return None
    rows = []
    for obs in data:
        if obs["value"] == ".":
            continue
        rows.append({"date": obs["date"], "value": float(obs["value"])})
    df = pd.DataFrame(rows, columns=["date", "value"])
    df["date"] = pd.to_datetime(df["date"])
    df["series_id"] = series_id
    return df


def fetch_all(days: int = 365 * 5) -> dict[str, pd.DataFrame]:
    result = {}
    for sid in TICKERS_FRED:
        df = fetch_series(sid, days)
        if df is not None:
            result[sid] = df
    return result
