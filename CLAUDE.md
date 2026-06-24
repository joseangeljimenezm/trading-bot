# Trading Bot — Manual del Sistema

## Objetivo
Sistema multi-activo semi-automático con 8 señales tácticas.
- Rentabilidad objetivo: 2% mensual (~26.8% anual)
- Drawdown máximo aceptable: -35%
- Perfil: agresivo
- Capital virtual paper trading: $100,000

## Stack
- Python 3.12, `ib_insync`, `yfinance`, `supabase-py`, `python-telegram-bot`
- Datos: yfinance (precios), FRED API (macroeconomía), CoinGecko (crypto), Alternative.me (Fear & Greed)
- Almacenamiento: Supabase (PostgreSQL cloud)
- Automatización: GitHub Actions (6:00 CET, lunes a viernes)
- Notificaciones: Telegram

## Estructura del proyecto
```
C:\Trading\
├── .env                    # Credenciales (NO se sube a Git)
├── .env.example            # Plantilla de credenciales
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── sql/init_tables.sql     # SQL para crear tablas en Supabase
├── .github/workflows/
│   └── daily-pipeline.yml  # Workflow GitHub Actions
├── src/
│   ├── config.py           # Variables de entorno
│   ├── settings.py         # Parámetros ajustables (señales, riesgo, cartera)
│   ├── pipeline.py         # Orquestador principal
│   ├── portfolio.py        # Asignación por régimen
│   ├── risk.py             # Stop-loss, take-profit, sizing, comisiones
│   ├── scanner.py          # Escáner de oportunidades (genera informe completo)
│   ├── notifications.py    # Envío Telegram
│   ├── tracker.py          # Registro de posiciones en Supabase
│   ├── ibkr.py             # Generación de órdenes (simuladas/API)
│   ├── report.py           # Consulta histórica de señales
│   ├── models/
│   │   └── enums.py        # Regime, SignalVote, AssetClass
│   ├── data/
│   │   ├── yfinance_client.py
│   │   ├── fred_client.py
│   │   └── supabase_client.py
│   └── signals/
│       ├── base.py          # SignalResult dataclass
│       ├── orchestrator.py  # Votación ponderada
│       ├── dual_momentum.py # Señal 1
│       ├── canary.py        # Señal 2
│       ├── fed_regime.py    # Señal 3
│       ├── vix_regime.py    # Señal 4
│       ├── oil_shock.py     # Señal 5
│       ├── usd_trend.py     # Señal 6
│       ├── crypto_composite.py # Señal 7
│       └── liquidity.py     # Señal 8
└── tests/
```

## Las 8 señales (con pesos configurables en src/settings.py)

| # | Señal | Peso | Lógica |
|---|-------|------|--------|
| 1 | Dual Momentum | 25% | SPY 12m > BIL 12m alcista. VIX > 25 fuerza bajista |
| 2 | VIX Regime | 20% | <15 calma (alcista), 15-25 normal (neutral), 25-30 precaución, >30 pánico (bajista) |
| 3 | Canary | 15% | Correlación 20d SPY-HYG. <0.6 = pánico (bajista), >0.8 = normal (alcista) |
| 4 | Régimen Fed | 15% | Tipos ≤2% alcista, 2-5% neutral, >5% bajista + tendencia |
| 5 | Crypto Composite | 10% | BTC > SMA200 alcista + Fear & Greed <25 compra, >75 venta |
| 6 | USD Trend | 10% | UUP > SMA200 = USD fuerte alcista, < SMA200 = USD débil bajista |
| 7 | Liquidez Global | 5% | Fed balance (WALCL) trending up alcista, contracting bajista |
| 8 | Oil Shock | 5% | Petróleo >+10% en 30d bajista, <-10% alcista |

**Votación**: Ponderada. Cada señal vota bullish/bearish/neutral con su peso. Si gana bullish con >60% → RISK ON. Si gana bearish con >60% → RISK OFF. Si no → DISINFLATION.

## Cartera por régimen (configurable en settings.py)

| Régimen | SPY | QQQ | IWM | EEM | GLD | TLT | HYG | BTC | BIL |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| RISK ON | 20% | 10% | 10% | 5% | 10% | 10% | 10% | 5% | 20% |
| DISINFLATION | 15% | 5% | - | - | 15% | 20% | 5% | 5% | 35% |
| RISK OFF | - | - | - | - | 20% | 30% | - | - | 50% |
| STAGFLATION | 10% | - | 10% | - | 25% | 5% | - | - | 40% |
| CRASH | - | - | - | - | 15% | 25% | - | - | 60% |

## Gestión de riesgo
- Stop-loss por activo: -10% desde entry
- Take-profit inicial: +15% (vender 50%, dejar correr resto)
- Stop-loss cartera: -20% en 30d → reducir exposición 50%
- Drawdown máximo: -35% → detener sistema
- Cooldown: si pérdida >5% en 1 día, no operar al siguiente
- Máximo 30% en un solo activo
- Máximo 50% en una clase
- Crypto máximo 20% de la cartera

## Comisiones estimadas (IBKR Tiered)
- ETFs: ~$0.40 por operación
- Crypto (Kraken): ~$0.25 por operación
- Total mensual estimado (40 ops): ~$15-20
- Impacto en $100k: ~0.02% mensual

## Pipeline diario (GitHub Actions, 6:00 CET)
1. Fetch precios (yfinance, max histórico)
2. Fetch macro (FRED)
3. Calcular 8 señales → votación ponderada
4. Determinar régimen → cartera sugerida
5. Calcular órdenes (entry price, stop-loss, take-profit)
6. Guardar en Supabase
7. Enviar informe a Telegram

## Comandos útiles
```bash
python -X utf8 -m src.pipeline          # Ejecutar pipeline completo
python -X utf8 -m src.report            # Ver historial de señales
python -X utf8 -m src.report --days 30  # Últimos 30 días
```

## Credenciales (archivo .env, NO subir a Git)
```
FRED_API_KEY        → b4a59159f00614064e43a4cd6cf80c91
SUPABASE_URL        → https://ljjqlaukmscbrtpwpvae.supabase.co
SUPABASE_KEY        → service_role key
TELEGRAM_BOT_TOKEN  → 8879317689:AAGlEVQOx8A_RyCtopzb6zAe9FORLLVW4jU
TELEGRAM_CHAT_ID    → 6838763896
```

Estas mismas credenciales están almacenadas como GitHub Secrets para el workflow automático.

## Supabase (PostgreSQL cloud)
- Proyecto: trading-bot
- Tablas: raw_prices, fred_data, signal_log, portfolio_snapshots
- Las tablas se crean ejecutando sql/init_tables.sql en el SQL Editor

## IBKR (para paper trading futuro)
- Puerto paper: 7497
- Puerto live: 7496
- Módulo src/ibkr.py genera órdenes simuladas (texto). Con Gateway abierto, puede ejecutar automáticamente.

## Ajustar parámetros
Todo se configura desde `src/settings.py`:
- Pesos de señales: SIGNAL_CONFIG["señal"]["weight"]
- Umbrales: thresholds de cada señal
- Cartera por régimen: PORTFOLIO_CONFIG["regime_allocations"]
- Riesgo: RISK_CONFIG
