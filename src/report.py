"""Reporte de señales y cartera. Ejecutar: python -m src.report"""

from datetime import datetime, date, timedelta

from src.data.supabase_client import get_client, get_signal_history

HEADER = f"{'Señal':20s} {'Voto':10s} {'Detalle'}"
SEP = "-" * 80


def show_today():
    client = get_client()
    today = str(date.today())
    resp = client.table("signal_log").select("*").eq("date", today).execute()
    rows = resp.data
    if not rows:
        print("Sin datos para hoy.")
        return

    print(f"\nSeñales - {today}")
    print(SEP)
    print(HEADER)
    print(SEP)
    for r in sorted(rows, key=lambda x: x["signal_name"]):
        icon = {"bullish": "+", "bearish": "-", "neutral": "~"}.get(r["vote"], "?")
        print(f"{icon} {r['signal_name']:18s} {r['vote']:10s} {r.get('details', '') or ''}")
    print(SEP)


def show_history(days: int = 7):
    rows = get_signal_history(days)
    if not rows:
        print(f"Sin datos en los últimos {days} días.")
        return

    dates = sorted(set(r["date"] for r in rows), reverse=True)

    print(f"\nHistorial de señales (últimos {len(dates)} días)")
    print(SEP)

    for d in dates:
        day_rows = [r for r in rows if r["date"] == d]
        votes = [r["vote"] for r in day_rows]
        bull = votes.count("bullish")
        bear = votes.count("bearish")
        neutral = votes.count("neutral")
        print(f"\n{d}")
        for r in sorted(day_rows, key=lambda x: x["signal_name"]):
            icon = {"bullish": "+", "bearish": "-", "neutral": "~"}.get(r["vote"], "?")
            print(f"  {icon} {r['signal_name']:18s} {r['vote']:8s}")
        print(f"  {'':->40s}")
        print(f"  Total: {bull} alcistas, {bear} bajistas, {neutral} neutrales")
    print(SEP)


def show_allocation():
    """Muestra la última asignación de cartera."""
    client = get_client()
    resp = client.table("portfolio_snapshots").select("*").order("date", desc=True).limit(1).execute()
    snapshots = resp.data
    if not snapshots:
        print("Sin datos de cartera.")
        return

    snap = snapshots[0]
    import json
    positions = json.loads(snap["positions"]) if isinstance(snap["positions"], str) else snap["positions"]
    print(f"\nCartera sugerida - {snap['date']} | Régimen: {snap.get('regime', '?')} | Valor: {snap.get('total_value', '?')}")
    print(SEP)
    print(f"{'Activo':10s} {'%':>6s}")
    print(SEP)
    for ticker, pct in sorted(positions.items(), key=lambda x: -x[1]):
        print(f"{ticker:10s} {pct*100:5.1f}%")
    print(SEP)


def main():
    show_today()
    show_history(7)
    print("\nPara ver el historial completo:")
    print("  python -m src.report --days 30")


if __name__ == "__main__":
    import sys
    days = 7
    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        if idx + 1 < len(sys.argv):
            days = int(sys.argv[idx + 1])
    show_today()
    show_history(days)
