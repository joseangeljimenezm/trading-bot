from src.models.enums import Regime, SignalVote


BASE_ALLOCATIONS = {
    Regime.RISK_ON: {
        "SPY": 0.20,
        "QQQ": 0.10,
        "IWM": 0.10,
        "EEM": 0.05,
        "GLD": 0.10,
        "TLT": 0.10,
        "HYG": 0.10,
        "BTC": 0.05,
        "BIL": 0.20,
    },
    Regime.DISINFLATION: {
        "SPY": 0.15,
        "QQQ": 0.05,
        "GLD": 0.15,
        "TLT": 0.20,
        "HYG": 0.05,
        "BTC": 0.05,
        "BIL": 0.35,
    },
    Regime.RISK_OFF: {
        "GLD": 0.20,
        "TLT": 0.30,
        "BIL": 0.50,
    },
    Regime.STAGFLATION: {
        "GLD": 0.25,
        "DBC": 0.10,
        "BIL": 0.40,
        "TLT": 0.05,
        "SPY": 0.10,
        "IWM": 0.10,
    },
    Regime.CRASH: {
        "GLD": 0.15,
        "TLT": 0.25,
        "BIL": 0.60,
    },
}


def compute_allocation(regime: Regime, confidence: float) -> dict[str, float]:
    base = BASE_ALLOCATIONS.get(regime, BASE_ALLOCATIONS[Regime.DISINFLATION])
    if confidence > 0.8:
        return base
    if confidence > 0.6:
        return {k: v * 0.9 for k, v in base.items()}
    neutral = BASE_ALLOCATIONS[Regime.DISINFLATION]
    blended = {}
    all_keys = set(base) | set(neutral)
    blend_factor = 0.6 if regime == Regime.RISK_ON else 0.4
    for k in all_keys:
        blended[k] = base.get(k, 0) * blend_factor + neutral.get(k, 0) * (1 - blend_factor)
    total = sum(blended.values())
    return {k: v / total for k, v in blended.items()}
