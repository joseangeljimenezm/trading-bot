"""Gestión de riesgo: stop-loss, take-profit, sizing, comisiones."""

from dataclasses import dataclass

import yfinance as yf

from src.settings import RISK_CONFIG, PORTFOLIO_CONFIG

STOP_LOSS_PCT = RISK_CONFIG["stop_loss_pct"]
TAKE_PROFIT_PCT = RISK_CONFIG["take_profit_pct"]
PORTFOLIO_VIRTUAL = PORTFOLIO_CONFIG["virtual_capital"]

# Comisiones estimadas IBKR Tiered
FEES = {
    "SPY": 0.40,
    "QQQ": 0.40,
    "IWM": 0.40,
    "EEM": 0.40,
    "GLD": 0.40,
    "TLT": 0.40,
    "HYG": 0.40,
    "BIL": 0.40,
    "DBC": 0.40,
    "BTC": 0.25,  # Kraken
    "ETH": 0.25,
}


@dataclass
class PositionPlan:
    ticker: str
    target_pct: float
    entry_price: float
    stop_loss: float
    take_profit: float
    quantity: int
    amount: float
    fee: float
    evidence: str


def get_current_price(ticker: str) -> float | None:
    try:
        df = yf.download(ticker, period="2d", auto_adjust=True, progress=False)
        if not df.empty:
            return float(df["Close"].squeeze().iloc[-1])
    except Exception:
        pass
    return None


def compute_positions(allocation: dict[str, float]) -> list[PositionPlan]:
    plans = []
    for ticker, pct in sorted(allocation.items(), key=lambda x: -x[1]):
        price = get_current_price(ticker)
        if price is None or price <= 0:
            continue
        amount = PORTFOLIO_VIRTUAL * pct
        quantity = max(1, int(amount / price))
        actual_amount = quantity * price
        sl = round(price * (1 - STOP_LOSS_PCT), 2)
        tp = round(price * (1 + TAKE_PROFIT_PCT), 2)
        fee = FEES.get(ticker, 0.40)
        evidence = _generate_evidence(ticker, pct)
        plans.append(PositionPlan(ticker, pct, price, sl, tp, quantity, actual_amount, fee, evidence))
    return plans


def estimate_monthly_fees(plans: list[PositionPlan]) -> dict:
    """Estima comisiones mensuales (~40 operaciones/mes según arquitectura)."""
    entry_fees = sum(p.fee for p in plans)
    exit_fees = sum(p.fee for p in plans)
    monthly_trades = 40
    etf_count = sum(1 for p in plans if p.ticker != "BTC")
    crypto_count = sum(1 for p in plans if p.ticker == "BTC")
    etf_fee_per_trade = 0.40
    crypto_fee_per_trade = 0.25
    monthly_etf_fees = monthly_trades * etf_fee_per_trade * (etf_count / max(1, len(plans)))
    monthly_crypto_fees = monthly_trades * crypto_fee_per_trade * (crypto_count / max(1, len(plans)))
    return {
        "entry_fees": entry_fees,
        "exit_fees": exit_fees,
        "round_trip": entry_fees + exit_fees,
        "monthly_estimate": round(monthly_etf_fees + monthly_crypto_fees, 2),
        "monthly_breakdown": f"ETFs ~${monthly_etf_fees:.0f} + Crypto ~${monthly_crypto_fees:.0f}",
    }


def _generate_evidence(ticker: str, pct: float) -> str:
    evidences = {
        "SPY": "Dual Momentum + VIX < 25 → Riesgo ON. S&P 500 en tendencia alcista 12m.",
        "QQQ": "Tecnología líder en mercado alcista. Nasdaq con fuerza relativa.",
        "IWM": "Small caps siguen tendencia si RISK ON se consolida.",
        "EEM": "Emergentes con USD fuerte → cautela. Peso reducido al 5%.",
        "GLD": "Oro como cobertura. Petróleo bajando + Fed bajando tipos → favorable.",
        "TLT": "Bonos largos. Petróleo -25% en 30d → señal de compra. Tipos bajando.",
        "HYG": "High yield con correlación SPY > 0.8 → mercado normal, sin pánico.",
        "BIL": "Reserva de liquidez. 20% en cash para oportunidades o protección.",
        "BTC": "Crypto bajista (BTC bajo SMA200). Peso mínimo al 5%. Fear & Greed 17 podría ser oportunidad de acumulación.",
        "DBC": "Commodities. Petróleo en shock bajista → presión general.",
    }
    return evidences.get(ticker, "Asignación táctica según régimen actual.")
