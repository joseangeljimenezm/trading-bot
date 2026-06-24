# ESTRATEGIA DE DATOS — Fuentes, Valor y Conexión con Señales

> Objetivo: Definir exactamente qué datos necesitamos, de dónde los sacamos y por qué valen algo.

---

## 1. MAPA COMPLETO DE FUENTES

### Fuentes imprescindibles (sin esto no hay sistema)

| Fuente | Tipo | Lo que da | ¿Cómo lo obtenemos? |
|--------|------|-----------|---------------------|
| **FRED API** | API REST | Macro: tipos, inflación, VIX, petróleo, yields, liquidez | `api.stlouisfed.org/fred/series/observations` — JSON |
| **Yahoo Finance** | API (yfinance) | Precios diarios de ETFs y activos | `yfinance` Python — OHLCV directo |
| **CoinGecko** | API REST | Precios crypto, dominancia, market cap (si incluimos crypto) | `api.coingecko.com/api/v3/` — JSON |

### Fuentes complementarias (dan contexto táctico)

| Fuente | Tipo | Lo que da | ¿Cómo lo obtenemos? |
|--------|------|-----------|---------------------|
| **Alternative.me** | API REST | Crypto Fear & Greed Index | `api.alternative.me/fng/` — JSON |
| **USTR RSS Feed** | RSS/XML | Anuncios de aranceles Section 301 | `ustr.gov/press-releases/feed` — XML parseable |
| **White House RSS** | RSS/XML | Órdenes ejecutivas, trade policy | `whitehouse.gov/feed` — XML parseable |

### Fuentes que NO usamos (y por qué)

| Fuente | Razón del descarte |
|--------|--------------------|
| **TIC (US Treasury)** | Datos con 6 semanas de retraso. Para trading a corto es historia. Solo vale como contexto macro trimestral. |
| **SEC EDGAR 13F** | 45 días de retraso. Las ballenas ya movieron el mercado. Sin valor táctico. |
| **CFTC COT** | Formato fixed-width, requiere parseo complejo, beneficio marginal. Lo recuperamos si vemos que falta algo. |
| **Investing.com Calendar** | Scraping frágil (cambian HTML). Preferimos fuentes oficiales directas. |
| **Glassnode / CryptoQuant** | Pagado. Si el sistema funciona sin él, no lo necesitamos. |
| **Arkham Intelligence** | Pagado el tier útil. Gratis solo da lo que CoinGecko ya da. |

---

## 2. DATOS ESPECÍFICOS QUE EXTRAEMOS (por señal)

### Señal 1: Dual Momentum
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| SPY precio cierre ajustado | yfinance | `SPY` — Adjusted Close | Diaria |
| BIL precio cierre ajustado | yfinance | `BIL` — Adjusted Close | Diaria |

**Valor**: La señal más probada históricamente. Si el S&P 500 rinde más que cash, estar invertido. Simple, funciona.

### Señal 2: Canary (SPY vs HYG)
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| SPY precio cierre | yfinance | `SPY` — Close | Diaria |
| HYG precio cierre | yfinance | `HYG` — Close | Diaria |

**Valor**: Alta. La correlación entre investment grade y high yield se rompe ANTES de las correcciones. Es un leading indicator real.

### Señal 3: Régimen Fed
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| Fed Funds Rate | FRED | `FEDFUNDS` | Diaria |
| 10-Year Yield | FRED | `DGS10` | Diaria |
| 2-Year Yield | FRED | `DGS2` | Diaria |
| Yield Curve Spread | FRED | `T10Y2Y` | Diaria (derivado) |

**Valor**: Alta. La Fed marca el régimen macro. Saber si estamos en 0-2%, 2-5% o 5-10% cambia qué activos funcionan.

### Señal 4: VIX Regime
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| CBOE VIX | FRED | `VIXCLS` | Diaria |

**Valor**: Alta. VIX > 25 es precaución. VIX > 30 es pánico. VIX < 15 es complacencia. Cambia TODO el position sizing.

### Señal 5: Petróleo Shock
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| WTI Crude Oil | FRED | `DCOILWTICO` | Semanal (FRED) |
| WTI Crude Oil | yfinance | `CL=F` — Close | Diaria |

Vía yfinance es más actual. FRED para contexto histórico.

**Valor**: Media. Petróleo +10% afecta TLT y GLD. Pero no es una señal frecuente (~4-6 veces/año).

### Señal 6: USD Trend
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| USD Index ETF | yfinance | `UUP` — Close | Diaria |

**Valor**: Media. El dólar mueve VXUS, GLD, EEM. Pero es más lento, tendencias de meses.

### Señal 7: Crypto Composite
| Dato | Fuente | Endpoint | Frecuencia |
|------|--------|----------|------------|
| BTC precio | CoinGecko | `/coins/bitcoin/market_chart/range` | Horaria |
| ETH precio | CoinGecko | `/coins/ethereum/market_chart/range` | Horaria |
| BTC Dominancia | CoinGecko | `/global` | Diaria |
| Crypto Total MC | CoinGecko | `/global` | Diaria |
| Fear & Greed | Alternative.me | `/fng/?limit=30` | Diaria |

**Valor**: Alta cuando estamos en régimen crypto alcista. Nula en mercado bajista. Se activa cuando BTC > 200d MA.

### Señal 8: Liquidez Global
| Dato | Fuente | Serie/Endpoint | Frecuencia |
|------|--------|---------------|------------|
| Fed Balance Sheet | FRED | `WALCL` | Semanal |
| Real Yield 10Y TIPS | FRED | `DFII10` | Diaria |

**Valor**: Alta. **Este es el dato que menos gente mira.** Cuando la Fed imprime dinero (WALCL sube), todo sube. Cuando contrae balance, todo baja. El real yield es el verdadero driver del oro (no la inflación nominal).

---

## 3. MAPA DE VALOR — Prioridad de datos

```
VALOR ALTO (imprescindibles):
├── FEDFUNDS    → saber régimen de tipos
├── VIXCLS      → saber si hay pánico
├── SPY cierre   → Dual Momentum, Canary
├── HYG cierre   → Canary
├── GLD cierre   → performance oro
├── TLT cierre   → performance bonos
├── BIL cierre   → Dual Momentum base
├── WALCL        → liquidez Fed (poco conocido)
├── DFII10       → real yield → driver oro

VALOR MEDIO (complementos tácticos):
├── UUP cierre  → USD trend
├── CL=F cierre → oil shock
├── BTC/ETH     → crypto overlay
├── USTR RSS    → aranceles → FXI/QQQ

VALOR BAJO (solo contexto):
├── TIC data    → 6 semanas retraso
├── 13F filings → 45 días retraso
├── COFER       → trimestral
```

---

## 4. FRECUENCIA DE ACTUALIZACIÓN

| Frecuencia | Datos | Cuándo se actualizan |
|------------|-------|----------------------|
| **Diaria** | Precios ETFs, crypto, VIX, FEDFUNDS, yields | Cada mañana antes de mercado (8:00 CET) |
| **Semanal** | WALCL (Fed balance), inventarios petróleo | Miércoles |
| **Mensual** | CPI, Unemployment, TIC | Día de publicación del dato |
| **Eventos** | USTR RSS, White House RSS | En tiempo real (check cada hora) |

---

## 5. RATE LIMITS Y PLANES GRATUITOS

| Fuente | Límite | ¿Suficiente para diario? |
|--------|--------|--------------------------|
| **FRED API** | 1,000 calls/hora | ✅ Sí (necesitamos ~15 calls/día) |
| **yfinance** | No hay límite documentado | ✅ Sí |
| **CoinGecko** | 30 calls/minuto, 10-15k/mes | ✅ Sí (necesitamos ~50 calls/día) |
| **Alternative.me** | Sin límite documentado | ✅ Sí (1 call/día) |
| **USTR RSS** | Sin límite | ✅ Sí |

**Conclusión**: Con planes gratuitos tenemos datos de sobra.

---

## 6. ¿QUÉ DATOS DAN VENTAJA REAL?

El 90% de los traders tienen acceso a precios y gráficos. La ventaja NO está en tener más datos, sino en:

### Ventaja 1: Detección de régimen ANTES del consenso
- FEDFUNDS + T10Y2Y + WALCL → sabes si la liquidez aumenta o disminuye
- La mayoría mira solo precio. Nosotros miramos la CAUSA (liquidez, tipos)

### Ventaja 2: Correlaciones rotas = señal temprana
- HYG vs SPY divergencia → 1-2 semanas ANTES de la corrección
- La mayoría descubre la divergencia cuando ya es obvia

### Ventaja 3: Automatización de señales compuestas
- 8 señales votando cada día → decisión objetiva, sin sesgo emocional
- La mayoría opera por instinto o noticias

### Ventaja 4: Crypto como overlay táctico (no como core)
- Fear & Greed + BTC dominancia + 200d MA → entradas en ciclos
- Sin estar siempre expuesto al crypto winter

---

## 7. DIAGRAMA DE FLUJO DE DATOS

```
DIARIO (8:00 CET):
  FRED ──→ FEDFUNDS, VIXCLS, DGS10, DGS2, T10Y2Y, DFII10, WALCL
              ↓
  yfinance ──→ SPY, GLD, TLT, HYG, BIL, UUP, QQQ, IWM, XLE, XLU, CL=F
              ↓
  CoinGecko ──→ BTC price, ETH price, BTC Dominance, Total MC
              ↓
  Alternative ──→ Fear & Greed Index
              ↓
         ┌─────┴──────┐
         │  SIGNALS    │
         │  (8 reglas) │
         └─────┬──────┘
               ↓
         ┌─────┴──────┐
         │  DECISION   │
         │  (votación) │
         └─────┬──────┘
               ↓
         ┌─────┴──────┐
         │  ALERTA     │
         │  (Telegram) │
         └────────────┘

EVENTOS (cada hora):
  USTR RSS ──→ keyword match ──→ ALERTA (si hay arancel nuevo)
  White House RSS ──→ keyword match ──→ ALERTA (si hay trade policy)
```

---

## 8. DECISIONES ABIERTAS (para ti)

1. **Crypto**: CoinGecko gratis + Alternative.me = suficiente para empezar. Cuando decidamos exchange, añadimos.
2. **Almacenamiento**: Prefiero SQLite (un solo archivo, fácil de respaldar y transportar) vs CSVs (múltiples archivos). ¿Opinión?
3. **Histórico**: FRED da 70+ años, yfinance da ~10 años. Para backtesting necesitamos mínimo 5 años. Con 10 mejor.

¿Confirmas este planteamiento de datos antes de pasar al diseño del modelo de almacenamiento?
