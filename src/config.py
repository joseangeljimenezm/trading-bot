import os
from dotenv import load_dotenv

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY", "")
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# --- Universo de activos ---
# Señales calculadas con tickers US
TICKERS_US = {
    "SPY": "S&P 500",
    "GLD": "Oro",
    "TLT": "Bonos Largo Plazo",
    "HYG": "High Yield",
    "IWM": "Small Caps",
    "VWO": "Emergentes",
    "DBC": "Commodities",
    "EEM": "Mercados Emergentes",
}

# Ejecución en ETFs UCITS (compatibles Europa)
TICKERS_UCITS = {
    "CSPX": "S&P 500 UCITS",
    "IGLN": "Oro UCITS",
    "DTLA": "Bonos Largo UCITS",
    "SHYG": "High Yield UCITS",
    "IWDA": "MSCI World UCITS",
    "IS3N": "Emergentes UCITS",
    "ERNS": "Commodities UCITS",
}

TICKERS_FRED = {
    "DGS10": "T-bond 10y",
    "DGS2": "T-bond 2y",
    "T10Y2Y": "Pendiente 10-2",
    "T5YIE": "Breakeven 5y",
    "UNRATE": "Tasa de Paro",
    "CPIAUCSL": "IPC",
    "FEDFUNDS": "Tasa Fed",
    "BAMLH0A0HYM2": "HY Spread",
    "VIXCLS": "VIX",
    "USREC": "Recesión",
}
