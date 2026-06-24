from enum import StrEnum


class Regime(StrEnum):
    RISK_ON = "risk_on"
    RISK_OFF = "risk_off"
    STAGFLATION = "stagflation"
    DISINFLATION = "disinflation"
    CRASH = "crash"


class SignalVote(StrEnum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    NEUTRAL = "neutral"


class AssetClass(StrEnum):
    EQUITY = "equity"
    BOND = "bond"
    GOLD = "gold"
    COMMODITY = "commodity"
    CRYPTO = "crypto"
    CASH = "cash"
