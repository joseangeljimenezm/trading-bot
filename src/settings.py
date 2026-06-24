"""Configuración ajustable de señales, riesgo y pesos."""

SIGNAL_CONFIG = {
    "dual_momentum": {
        "weight": 0.25,
        "lookback_days": 252,
        "vix_threshold": 25,
    },
    "vix_regime": {
        "weight": 0.20,
        "calm_threshold": 15,
        "caution_threshold": 25,
        "panic_threshold": 30,
    },
    "canary": {
        "weight": 0.15,
        "correlation_window": 20,
        "risk_off_threshold": 0.6,
        "risk_on_threshold": 0.8,
    },
    "fed_regime": {
        "weight": 0.15,
        "low_rate": 2.0,
        "high_rate": 5.0,
    },
    "crypto_composite": {
        "weight": 0.10,
        "btc_trend_weight": 0.6,
        "fg_extreme_fear": 25,
        "fg_extreme_greed": 75,
    },
    "usd_trend": {
        "weight": 0.10,
        "sma_period": 200,
    },
    "liquidity": {
        "weight": 0.05,
        "expansion_threshold": 0.01,
        "contraction_threshold": -0.01,
        "lookback_days": 30,
    },
}

RISK_CONFIG = {
    "stop_loss_pct": 0.10,
    "take_profit_pct": 0.15,
    "portfolio_drawdown_limit": 0.35,
    "portfolio_stop_loss_30d": 0.20,
    "daily_loss_cooldown": 0.05,
    "max_single_asset_pct": 0.30,
    "max_single_class_pct": 0.50,
    "crypto_max_pct": 0.20,
    "cash_min_pct": 0.10,
    "cash_max_pct": 1.00,
}

PORTFOLIO_CONFIG = {
    "virtual_capital": 100_000,
    "regime_allocations": {
        "risk_on": {
            "SPY": 0.20, "QQQ": 0.10, "IWM": 0.10, "EEM": 0.05,
            "GLD": 0.10, "TLT": 0.10, "HYG": 0.10, "BTC": 0.05, "BIL": 0.20,
        },
        "disinflation": {
            "SPY": 0.15, "QQQ": 0.05, "GLD": 0.15, "TLT": 0.20,
            "HYG": 0.05, "BTC": 0.05, "BIL": 0.35,
        },
        "risk_off": {
            "GLD": 0.20, "TLT": 0.30, "BIL": 0.50,
        },
        "stagflation": {
            "GLD": 0.25, "DBC": 0.10, "BIL": 0.40,
            "TLT": 0.05, "SPY": 0.10, "IWM": 0.10,
        },
        "crash": {
            "GLD": 0.15, "TLT": 0.25, "BIL": 0.60,
        },
    },
}
