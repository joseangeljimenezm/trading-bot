from datetime import datetime

from src.data.supabase_client import upsert_prices, upsert_fred
from src.data.yfinance_client import fetch_all as fetch_prices
from src.data.fred_client import fetch_all as fetch_fred
from src.signals.orchestrator import compute_all_signals, vote, regime_from_vote
from src.portfolio import compute_allocation
from src.notifications import send_signal_report


def run_pipeline(save_to_db: bool = True, send_telegram: bool = True):
    now = datetime.now()
    print(f"[{now:%Y-%m-%d %H:%M}] Iniciando pipeline...")

    prices = fetch_prices()
    for ticker, df in prices.items():
        print(f"  {ticker}: {len(df)} días")
        if save_to_db:
            upsert_prices(df)

    fred = fetch_fred()
    for sid, df in fred.items():
        print(f"  FRED {sid}: {len(df)} registros")
        if save_to_db:
            upsert_fred(df)

    signals = compute_all_signals()
    vote_result, confidence = vote(signals)
    regime = regime_from_vote(vote_result, confidence)
    allocation = compute_allocation(regime, confidence)

    print(f"\n--- VOTACIÓN ---")
    print(f"Voto: {vote_result.value.upper()} | Confianza: {confidence:.0%} | Régimen: {regime.value}")
    for s in signals:
        print(f"  {s.signal_name:20s} -> {s.vote.value:8s} | {s.details}")

    print(f"\n--- CARTERA SUGERIDA ---")
    for ticker, pct in sorted(allocation.items(), key=lambda x: -x[1]):
        print(f"  {ticker:6s}: {pct:5.1%}")

    if send_telegram:
        ok = send_signal_report(vote_result.value, confidence, regime.value, signals, allocation)
        print(f"\n  Telegram: {'✅ enviado' if ok else '❌ falló'}")

    print(f"[{datetime.now():%Y-%m-%d %H:%M}] Pipeline completado.")


def main():
    run_pipeline()


if __name__ == "__main__":
    main()
