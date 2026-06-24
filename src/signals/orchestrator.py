from src.models.enums import SignalVote, Regime
from src.signals.base import SignalResult
from src.signals.dual_momentum import compute_dual_momentum
from src.signals.canary import compute_canary
from src.signals.fed_regime import compute_fed_regime
from src.signals.vix_regime import compute_vix_regime
from src.signals.oil_shock import compute_oil_shock
from src.signals.usd_trend import compute_usd_trend
from src.signals.crypto_composite import compute_crypto_composite
from src.signals.liquidity import compute_liquidity

SIGNAL_WEIGHTS = {
    "dual_momentum": 0.25,
    "vix_regime": 0.20,
    "canary": 0.15,
    "fed_regime": 0.15,
    "crypto_composite": 0.10,
    "usd_trend": 0.10,
    "liquidity": 0.05,
}


def compute_all_signals() -> list[SignalResult]:
    results = []
    for name, fn in [
        ("dual_momentum", compute_dual_momentum),
        ("canary", compute_canary),
        ("fed_regime", compute_fed_regime),
        ("vix_regime", compute_vix_regime),
        ("oil_shock", compute_oil_shock),
        ("usd_trend", compute_usd_trend),
        ("crypto_composite", compute_crypto_composite),
        ("liquidity", compute_liquidity),
    ]:
        try:
            r = fn()
        except Exception as e:
            r = SignalResult(name, SignalVote.NEUTRAL, 0.0, f"error: {e}")
        results.append(r)
    return results


def vote(results: list[SignalResult]) -> tuple[SignalVote, float]:
    bull = 0.0
    bear = 0.0
    for r in results:
        w = SIGNAL_WEIGHTS.get(r.signal_name, 0.05) * r.weight
        if r.vote == SignalVote.BULLISH:
            bull += w
        elif r.vote == SignalVote.BEARISH:
            bear += w
    if bull > bear:
        return SignalVote.BULLISH, bull / (bull + bear)
    if bear > bull:
        return SignalVote.BEARISH, bear / (bull + bear)
    return SignalVote.NEUTRAL, 0.5


def regime_from_vote(vote: SignalVote, confidence: float) -> Regime:
    if vote == SignalVote.BULLISH and confidence > 0.6:
        return Regime.RISK_ON
    if vote == SignalVote.BEARISH and confidence > 0.6:
        return Regime.RISK_OFF
    return Regime.DISINFLATION
