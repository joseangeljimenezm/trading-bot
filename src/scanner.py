"""Escáner de oportunidades: genera el informe completo de mercado."""

from dataclasses import dataclass
from datetime import datetime

from src.models.enums import Regime
from src.signals.orchestrator import compute_all_signals, vote, regime_from_vote
from src.portfolio import compute_allocation
from src.risk import compute_positions, estimate_monthly_fees, PositionPlan
from src.signals.base import SignalResult


@dataclass
class ScanReport:
    date: str
    regime: str
    vote: str
    confidence: float
    signals: list[SignalResult]
    allocation: dict[str, float]
    positions: list[PositionPlan]
    fees: dict
    summary: str


def run_scan() -> ScanReport:
    signals = compute_all_signals()
    vote_result, confidence = vote(signals)
    regime = regime_from_vote(vote_result, confidence)
    allocation = compute_allocation(regime, confidence)
    positions = compute_positions(allocation)
    fees = estimate_monthly_fees(positions)
    summary = _build_summary(vote_result.value, confidence, regime, signals, positions, fees)
    return ScanReport(
        date=datetime.now().strftime("%d/%m/%Y %H:%M"),
        regime=regime.value,
        vote=vote_result.value,
        confidence=confidence,
        signals=signals,
        allocation=allocation,
        positions=positions,
        fees=fees,
        summary=summary,
    )


def _build_summary(vote: str, confidence: float, regime: Regime, signals: list[SignalResult], positions: list[PositionPlan], fees: dict) -> str:
    bull = sum(1 for s in signals if s.vote.value == "bullish")
    bear = sum(1 for s in signals if s.vote.value == "bearish")
    neutral = sum(1 for s in signals if s.vote.value == "neutral")

    invert = {"bullish": "ALCISTA", "bearish": "BAJISTA", "neutral": "NEUTRAL"}
    regime_names = {
        "risk_on": "RIESGO ON (mercado alcista)",
        "risk_off": "RIESGO OFF (protección)",
        "disinflation": "DESINFLACIÓN (neutral)",
        "stagflation": "ESTANFLACIÓN",
        "crash": "CRASH",
    }
    regime_name = regime_names.get(regime.value, regime.value)

    lines = [
        f"ESCANER DE OPORTUNIDADES — {datetime.now().strftime('%d/%m/%Y')}",
        f"{'=' * 40}",
        f"",
        f"REGIMEN: {regime_name}",
        f"VOTO: {vote.upper()} | Confianza: {confidence:.0%}",
        f"Señales: {bull} alcistas, {bear} bajistas, {neutral} neutrales",
        f"",
        f"SEÑALES DETALLADAS:",
    ]
    for s in signals:
        icon = {"bullish": "+", "bearish": "-", "neutral": "~"}.get(s.vote.value, "?")
        lines.append(f"  {icon} {s.signal_name}: {s.details}")
    lines.append("")
    lines.append(f"CARTERA Y EJECUCION:")
    lines.append(f"{'-' * 40}")
    total_invested = 0
    for p in positions:
        lines.append(f"{p.ticker} | {p.target_pct:.0%} | {p.quantity} acc | Entry: ${p.entry_price:.2f}")
        lines.append(f"  SL: ${p.stop_loss:.2f} ({-STOP_LOSS_PCT*100:.0f}%) | TP: ${p.take_profit:.2f} (+{TAKE_PROFIT_PCT*100:.0f}%)")
        lines.append(f"  Importe: ${p.amount:,.0f} | Comisión: ${p.fee:.2f}")
        lines.append(f"  Evidencia: {p.evidence}")
        total_invested += p.amount

    lines.append("")
    lines.append(f"RESUMEN ECONOMICO:")
    lines.append(f"{'-' * 40}")
    lines.append(f"Capital virtual: $100,000")
    lines.append(f"Invertido: ${total_invested:,.0f}")
    lines.append(f"En efectivo (BIL): ${100_000 - total_invested:,.0f}")
    lines.append(f"")
    lines.append(f"COMISIONES ESTIMADAS:")
    lines.append(f"  Por entrada: ${fees['entry_fees']:.2f}")
    lines.append(f"  Por salida: ${fees['exit_fees']:.2f}")
    lines.append(f"  Ida+vuelta: ${fees['round_trip']:.2f}")
    lines.append(f"  Estimación mensual (40 ops): ${fees['monthly_estimate']:.2f}")
    lines.append(f"  Desglose: {fees['monthly_breakdown']}")
    lines.append(f"  Impacto en $100k: -{fees['monthly_estimate'] / 100_000:.2%} mensual")
    lines.append(f"")
    lines.append(f"GESTION DE RIESGO:")
    lines.append(f"{'-' * 40}")
    lines.append(f"Stop-loss general: -10% por activo desde entrada")
    lines.append(f"Take-profit inicial: +15% por activo")
    lines.append(f"Stop-loss cartera: -20% en 30d → reducir exposición 50%")
    lines.append(f"Drawdown maximo: -35% → detener sistema")
    lines.append(f"Cool-down: si perdida >5% en 1 dia, no operar al siguiente")
    lines.append(f"")
    lines.append(f"CUANDO VENDER:")
    lines.append(f"{'-' * 40}")
    lines.append(f"Si señal cambia a BAJISTA para ese activo")
    lines.append(f"Si se alcanza Take Profit (+15%) → vender 50%, dejar correr el resto")
    lines.append(f"Si se alcanza Stop Loss (-10%) → vender TODO")
    lines.append(f"Si el regimen cambia a RISK OFF → reducir todo a GLD+TLT+BIL")
    lines.append(f"Si un activo pierde momentum relativo 3 dias seguidos → revisar")
    return "\n".join(lines)


STOP_LOSS_PCT = 0.10
TAKE_PROFIT_PCT = 0.15
