import yfinance as yf
import pandas as pd

from src.config import TICKERS_US


def fetch_prices(ticker: str, period: str = "5y") -> pd.DataFrame | None:
    try:
        df = yf.download(ticker, period=period, auto_adjust=True, progress=False)
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None
    if df.empty:
        return None
    df.columns = df.columns.get_level_values(0)
    df.columns = [c.lower() for c in df.columns]
    df["ticker"] = ticker
    df = df.reset_index().rename(columns={"Date": "date"})
    return df


def fetch_all(period: str = "max") -> dict[str, pd.DataFrame]:
    result = {}
    for ticker in TICKERS_US:
        df = fetch_prices(ticker, period)
        if df is not None:
            result[ticker] = df
    return result
