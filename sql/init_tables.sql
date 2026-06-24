-- Pega esto en Supabase Dashboard → SQL Editor → New Query → Run
-- Crea las tablas del sistema trading-bot

CREATE TABLE IF NOT EXISTS raw_prices (
    ticker TEXT NOT NULL,
    date DATE NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume BIGINT,
    PRIMARY KEY (ticker, date)
);

CREATE TABLE IF NOT EXISTS fred_data (
    series_id TEXT NOT NULL,
    date DATE NOT NULL,
    value REAL,
    PRIMARY KEY (series_id, date)
);

CREATE TABLE IF NOT EXISTS signal_log (
    date DATE NOT NULL,
    signal_name TEXT NOT NULL,
    vote TEXT NOT NULL,
    weight REAL,
    details TEXT,
    PRIMARY KEY (date, signal_name)
);

CREATE TABLE IF NOT EXISTS portfolio_snapshots (
    date DATE NOT NULL PRIMARY KEY,
    cash REAL,
    positions TEXT,
    total_value REAL,
    regime TEXT
);
