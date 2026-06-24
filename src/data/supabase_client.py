from datetime import date

import pandas as pd
from supabase import create_client, Client

from src.config import SUPABASE_URL, SUPABASE_KEY


_client: Client | None = None


def get_client() -> Client:
    global _client
    if _client is None:
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise RuntimeError("SUPABASE_URL y SUPABASE_KEY requeridos en .env")
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _client


def upsert_prices(df: pd.DataFrame):
    client = get_client()
    records = df.to_dict(orient="records")
    if not records:
        return
    for r in records:
        r["date"] = str(r["date"])[:10]
    client.table("raw_prices").upsert(records).execute()


def upsert_fred(df: pd.DataFrame):
    client = get_client()
    records = df.to_dict(orient="records")
    if not records:
        return
    for r in records:
        r["date"] = str(r["date"])[:10]
    client.table("fred_data").upsert(records).execute()


def save_signal_log(signal_name: str, vote: str, weight: float, details: str | None):
    client = get_client()
    today = str(date.today())
    client.table("signal_log").upsert({
        "date": today,
        "signal_name": signal_name,
        "vote": vote,
        "weight": weight,
        "details": details,
    }).execute()


def get_signal_history(days: int = 30) -> list[dict]:
    client = get_client()
    resp = client.table("signal_log").select("*").gte("date", str(date.today() - __import__("datetime").timedelta(days=days))).order("date", desc=True).execute()
    return resp.data
