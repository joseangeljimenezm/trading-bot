"""Tracker de cartera simulada en Supabase."""

from datetime import date
import json

from src.data.supabase_client import get_client
from src.risk import PositionPlan, PORTFOLIO_VIRTUAL


def open_positions(plans: list[PositionPlan], regime: str):
    """Registra las posiciones abiertas hoy en Supabase."""
    client = get_client()
    today = str(date.today())
    positions = []
    for p in plans:
        positions.append({
            "ticker": p.ticker,
            "quantity": p.quantity,
            "entry_price": p.entry_price,
            "stop_loss": p.stop_loss,
            "take_profit": p.take_profit,
            "amount": round(p.amount, 2),
        })
    client.table("portfolio_snapshots").upsert({
        "date": today,
        "cash": PORTFOLIO_VIRTUAL - sum(p.amount for p in plans),
        "positions": json.dumps(positions),
        "total_value": PORTFOLIO_VIRTUAL,
        "regime": regime,
    }).execute()


def get_open_positions() -> list[dict]:
    """Devuelve las últimas posiciones registradas."""
    client = get_client()
    resp = client.table("portfolio_snapshots").select("*").order("date", desc=True).limit(1).execute()
    if not resp.data:
        return []
    snap = resp.data[0]
    if isinstance(snap["positions"], str):
        snap["positions"] = json.loads(snap["positions"])
    return snap
