# ARQUITECTURA DEL SISTEMA DE TRADING

> Versión: 1.0  
> Objetivo: 2% mensual (~26.8% anual)  
> Drawdown máximo aceptable: -35%  
> Perfil: Agresivo, multi-activo, semi-automático → automático

---

## 1. UNIVERSO DE ACTIVOS

### Núcleo (IBKR — ETFs domiciliados US)
| Clase | Ticker | Descripción |
|-------|--------|-------------|
| Renta Variable US | SPY | S&P 500 |
| Renta Variable US | QQQ | Nasdaq 100 |
| Renta Variable US | IWM | Small Caps Russell 2000 |
| Renta Variable Global | VXUS | World ex-US |
| Emergentes | EEM | Emerging Markets |
| China | FXI | China Large Cap |
| Oro | GLD | Gold Spot |
| Plata | SLV | Silver Spot |
| Bonos Largos US | TLT | Treasury 20Y+ |
| Bonos Basura US | HYG | High Yield Corp |
| Cash | BIL | Treasury 1-3M |

### Sectores (IBKR — para rotación táctica)
| Ticker | Sector |
|--------|--------|
| XLE | Energía |
| XLF | Financieros |
| XLK | Tecnología |
| XLU | Utilidades |
| XLP | Consumo Defensivo |
| XLI | Industriales |
| XLB | Materiales |

### Crypto (Exchange: Kraken o Binance)
| Activo | Rol |
|--------|-----|
| BTC | Core crypto, reserva de valor digital |
| ETH | Smart contracts, DeFi |

### Si no hay acceso a ETFs US (Trade Republic), sustitutos UCITS:
| Clase | Ticker UCITS |
|-------|--------------|
| S&P 500 | CSPX |
| Oro | IGLN |
| Bonos Largos | DTLA (aprox) |
| Small Caps | IUSN |
| World | IWDA |
| Emerging | IS3N |

---

## 2. FUENTES DE DATOS

| Fuente | Datos | API | Frecuencia | Límites |
|--------|-------|-----|------------|---------|
| **FRED** | FEDFUNDS, CPIAUCSL, DGS10, VIXCLS, DCOILWTICO, T10Y2Y, DFII10, TICASSET, WALCL | REST JSON gratuita | Diaria | 1000 calls/hora |
| **yfinance** | Precios OHLCV de todos los ETFs | Python (yfinance) | Diaria | Sin límite real |
| **CoinGecko** | Precios BTC/ETH, exchange flows, dominancia, funding | REST gratuita (sin key) | Cada 5-60 min | 30 calls/min |
| **RSS Feeds** | USTR, White House, Fed, ECB | XML scraping | Eventos | Sin límite |
| **Alternative.me** | Crypto Fear & Greed Index | REST gratuita | Diaria | Sin límite |

---

## 3. SEÑALES (Sistema de 5+ reglas)

### Señal 1: Dual Momentum (SPY vs BIL)
- SPY 12m > BIL 12m → Riesgo ON
- SPY 12m < BIL 12m → Riesgo OFF (ir a BIL)
- Filtro VIX: si VIX > 25, forzar Riesgo OFF

### Señal 2: Canary (Correlación SPY-HYG)
- Rolling 20d correlation (SPY, HYG)
- Si < 0.6 → Riesgo OFF (pánico inminente)
- Si > 0.8 → Normal

### Señal 3: Régimen Fed
- FEDFUNDS en 0-2% → riesgo ON (SPY, QQQ, BTC)
- FEDFUNDS en 2-5% → GLD, SLV overweight
- FEDFUNDS en 5-10% → BIL, defensivo
- Trend: subiendo/bajando (leading)

### Señal 4: VIX Regime
- VIX < 15 → Calma absoluta. Riesgo ON (incluir HYG, EEM)
- VIX 15-25 → Normal. Estrategia base.
- VIX 25-30 → Precaución. Reducir riesgo, favor GLD, TLT
- VIX > 30 → Pánico. Solo GLD, TLT, BIL

### Señal 5: Petróleo Shock
- CL=F movió > 10% en 30d
- Sube >10% → vender TLT, comprar XLE, GLD
- Baja >10% → comprar TLT, vigilar HYG (recesión?)

### Señal 6: USD Trend
- UUP > 200d MA → USD fuerte. Vender VXUS, EEM, FXI
- UUP < 200d MA → USD débil. Comprar GLD, VXUS, EEM

### Señal 7: Crypto Composite
- BTC > 200d MA → trend ON
- Fear & Greed < 25 (extreme fear) → comprar
- BTC Dominancia > 60% → altcoins débiles, solo BTC
- ETH/BTC trending up → rotar a ETH

### Señal 8: Liquidez Global (Fed Balance Sheet)
- WALCL (Fed assets) trending up → Riesgo ON (todo sube con liquidez)
- WALCL contracting → Riesgo OFF
- Leading signal para mercados

---

## 4. PONDERACIÓN Y DECISIÓN

Cada señal vota con peso:
| Señal | Peso | Por qué |
|-------|------|---------|
| Dual Momentum | 25% | La más probada históricamente |
| VIX Regime | 20% | Captura pánico/calma |
| Canary (SPY-HYG) | 15% | Predictor de correcciones |
| Régimen Fed | 15% | Macro contexto |
| Crypto Composite | 10% | Solo cuando aplica |
| USD Trend | 10% | Secundario |
| Liquidez Global | 5% | Confirmación |

**Votación**: Consenso ponderado → Señal final: RISK ON, RISK OFF, o NEUTRAL

---

## 5. POSITION SIZING

### Reglas base:
- Máximo 30% en un solo activo
- Máximo 50% en una clase (ej. todos equities)
- Crypto: 0-20% según señal
- Cash/BIL: 10-100% según nivel de riesgo

### Volatilidad target:
- Ajustar tamaño para que volatilidad cartera no supere 20% anual
- Si un activo es muy volátil (BTC), reducir peso proporcionalmente

---

## 6. EJECUCIÓN (Semi-automático)

### Pipeline diario:
```
06:00 → Fetch data (FRED, yfinance, CoinGecko, RSS)
06:05 → Calcular las 8 señales
06:10 → Votación ponderada → Decisión
06:15 → Generar órdenes sugeridas
06:20 → Enviar alerta Telegram:
           "🟢 RISK ON | Peso: 80%
            Comprar: SPY (20%), GLD (15%), BTC (10%)
            Vender: TLT (-10%)"
06:30 → TÚ confirmas o ajustas órdenes
06:35 → Bot ejecuta en IBKR + Exchange
```

### Frecuencia operativa:
- Evaluación de señales: **diaria** (toma 5 min)
- Cambio de cartera: **cuando la señal cambia de régimen** (no a diario)
- Rebalanceo: **semanal** si no hay cambios de régimen
- 40 operaciones/mes ≈ 2/día → normal con entradas/salidas parciales

---

## 7. RIESGO Y CONTROLES

| Regla | Descripción |
|-------|-------------|
| Stop-loss por activo | -10% desde entrada |
| Stop-loss cartera | -20% en rolling 30d → reducir exposición 50% |
| Drawdown máximo | -35% → detener sistema, revisar señales |
| Crypto max weight | 20% de la cartera (aunque señal sea máx) |
| Correlación máxima | No tener >60% en activos correlacionados >0.7 |
| Cooldown post-loss | Si pérdida >5% en un día, no operar mañana |

---

## 8. COSTES ESTIMADOS

| Concepto | Coste | Impacto en 20k cartera |
|----------|-------|----------------------|
| Comisiones IBKR (40 ops/mes) | ~$28/mes | -0.14% mensual |
| Comisiones crypto (10 ops/mes) | ~$5/mes | -0.025% mensual |
| Diferenciales (slippage) | ~0.05% por op | -0.10% mensual |
| **Total costes** | **~$33/mes** | **-0.27% mensual** |

Necesitamos un 0.27% mensual solo para cubrir costes. Objetivo 2% neto = 2.27% bruto.

---

## 9. TECH STACK

| Componente | Tecnología |
|-------------|------------|
| Lenguaje | Python 3.12+ |
| Datos macro | `requests` → FRED API |
| Precios | `yfinance` |
| Crypto | `requests` → CoinGecko API |
| Señales | Pandas + NumPy |
| Broker tradicional | `ib_insync` (IBKR) |
| Crypto exchange | `python-kraken-sdk` o `python-binance` |
| Notificaciones | `python-telegram-bot` |
| Programación | Windows Task Scheduler (cada hora) |
| Logging | `loguru` |

---

## 10. FASES

| Fase | Duración | Qué se hace |
|------|----------|-------------|
| **Fase 0** | Ahora | Validar arquitectura (estás aquí) |
| **Fase 1** | 1 semana | Data layer: fetch FRED + yfinance + CoinGecko |
| **Fase 2** | 1 semana | Signal layer: 8 reglas implementadas |
| **Fase 3** | 1 semana | Decision layer: votación + position sizing |
| **Fase 4** | 1 semana | Backtesting con datos históricos |
| **Fase 5** | 1 semana | IBKR paper trading (sin dinero real) |
| **Fase 6** | 1 semana | Telegram alerts + semi-automático |
| **Fase 7** | En adelante | Dinero real con capital pequeño |

**Total estimado Fases 1-6: ~4-6 semanas**

---

> **Nota**: Este documento es el blueprint. Nada se codea hasta que tú confirmes cada punto.
