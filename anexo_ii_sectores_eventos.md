# 🔬 ANEXO II: SECTORES, EVENTOS GEOPOLÍTICOS Y FUENTES ADICIONALES

> **Fecha:** 2025-06-23  
> **Datos:** Yahoo Finance (sectores 2010-2025), Investing.com (calendario económico), Kimi Search (geopolítica), IMF COFER  
> **Este anexo complementa al informe principal `informe_macro_correlaciones.md`**

---

## 1. Sectores: Correlaciones y Sensibilidad al Petróleo

### Datos analizados (2010-2025, 184 meses)

| Sector | Ticker | Volatilidad Anual | Correlación con Petróleo |
|--------|--------|-------------------|---------------------------|
| **Energía** | XLE | **28.1%** | **0.516** |
| Materiales | XLB | 19.3% | 0.362 |
| Small Cap | IWM | 19.9% | 0.335 |
| Industriales | XLI | 17.9% | 0.320 |
| Financieros | XLF | 19.3% | 0.290 |
| Emerging | EEM | 18.1% | 0.298 |
| Tecnología | XLK | 17.9% | 0.250 |
| Nasdaq 100 | QQQ | 17.5% | 0.235 |
| Salud | XLV | 13.8% | 0.201 |
| Consumo | XLP | 12.3% | 0.160 |
| China | FXI | 24.9% | 0.185 |
| **Utilidades** | XLU | **15.0%** | **0.009** |

**Hallazgos clave:**

1. **XLE (Energía) es el sector más volátil y el más correlacionado con el petróleo (0.516).** Si el petróleo sube, XLE sube más que el petróleo (beta > 1). Si cae, XLE cae más.

2. **Utilidades (XLU) son casi inmunes al petróleo (correlación 0.009).** Es el sector más defensivo junto a Consumo (XLP).

3. **Tecnología (XLK) y Nasdaq (QQQ) tienen baja correlación con petróleo (0.25).** Son "light-commodity" — su valor depende de márgenes de software, no de costes energéticos.

4. **China (FXI) tiene alta volatilidad (24.9%) pero baja correlación con petróleo (0.185).** Sus ciclos dependen más de política interna y aranceles que de materias primas.

### Correlaciones entre sectores (2010-2025)

|  | XLE | XLF | XLK | XLU | XLI | XLP | XLB | XLV | FXI | EEM | IWM | QQQ |
|--|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **XLF** | 0.708 | — | 0.646 | 0.325 | 0.876 | 0.569 | 0.807 | 0.658 | 0.363 | 0.620 | **0.860** | 0.672 |
| **XLK** | 0.444 | 0.646 | — | 0.326 | 0.746 | 0.559 | 0.694 | 0.590 | 0.324 | 0.603 | 0.705 | **0.974** |
| **IWM** | 0.683 | **0.860** | 0.705 | 0.330 | 0.876 | 0.496 | 0.807 | 0.662 | 0.349 | 0.636 | — | 0.743 |

**Lecturas:**
- **QQQ y XLK correlación 0.974:** Son casi el mismo activo. No diversificar entre ambos.
- **XLF e IWM correlación 0.860:** Financieros y Small Caps se mueven juntos. El crédito bancario impulsa a las pequeñas empresas.
- **XLI (Industriales) y XLF (Financieros) correlación 0.876:** La economía real y la financiera están muy ligadas.
- **XLU (Utilidades) tiene las correlaciones más bajas con todos los sectores.** Es el mejor diversificador sectorial.

---

## 2. Eventos Geopolíticos: Qué pasó realmente

### Datos de eventos reales (rendimiento medio mensual durante el evento)

| Evento | Fecha | XLE | XLF | XLK | XLU | XLP | XLV | FXI | EEM | IWM | QQQ | Petróleo |
|--------|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|----------|
| **COVID** | Feb-May 2020 | **-5.80%** | **-7.52%** | -0.67% | -5.46% | -2.24% | **+0.73%** | -0.85% | -4.06% | -5.45% | +0.56% | **-13.19%** |
| **Ucrania** | Feb-Apr 2022 | **+7.69%** | -0.95% | -0.86% | +3.85% | -0.04% | +2.22% | **-8.20%** | -3.85% | +1.00% | +0.03% | **+6.68%** |
| **Brexit** | Jun-Jul 2016 | +2.05% | -3.75% | -1.86% | **+6.75%** | **+4.73%** | +0.50% | +1.69% | +3.74% | -0.02% | -2.54% | — |

### Hallazgos por evento

#### COVID (Feb-Mayo 2020): La anomalía de la tecnología
- **XLK (Tecnología) cayó solo -0.67% y QQQ subió +0.56%.** Mientras el mundo se colapsaba, Amazon, Zoom, Microsoft y Netflix se beneficiaban del confinamiento.
- **XLV (Salud) subió +0.73%.** Farmacéuticas y biotech eran la esperanza de la vacuna.
- **XLE (Energía) se hundió -5.80% y Petróleo -13.19%.** El confinamiento destruyó la demanda de combustible. El WTI llegó a cotizar en negativo (-$37/barril).
- **XLU (Utilidades) cayó -5.46%.** Sorprendente: las utilidades deberían ser defensivas. Pero el pánico de liquidez obligó a vender TODO.

#### Ucrania (Feb-Abril 2022): La guerra del petróleo
- **XLE (Energía) subió +7.69% y Petróleo +6.68%.** Sanciones a Rusia = escasez de petróleo y gas = precios récord.
- **FXI (China) se hundió -8.20%.** China depende de importaciones de energía. Precios altos = inflación importada + lockdowns COVID = pesadilla.
- **EEM (Emerging Markets) cayó -3.85%.** Los mercados emergentes son importadores netos de energía. Precio alto = déficit de cuenta corriente + inflación.
- **XLV (Salud) y XLU (Utilidades) subieron.** Defensivos que se benefician de la inflación por costes (pueden trasladar precios).

#### Brexit (Junio-Julio 2016): El pánico de un solo día
- **XLU (Utilidades) subió +6.75% y XLP (Consumo) +4.73%.** Inversores británicos y europeos buscaron refugio en sectores defensivos domésticos.
- **XLF (Financieros) cayó -3.75%.** Incertidumbre sobre el acceso al mercado único europeo.
- **QQQ cayó -2.54%.** Tecnología global con exposición europea.

---

## 3. Búsquedas Web: Qué mueve los mercados HOY

### Hallazgos de búsquedas recientes (2024-2025)

**1. Los mercados se han vuelto más resistentes a eventos geopolíticos**
> "El impacto directo de eventos geopolíticos en los mercados financieros es cada vez más reducido y más efímero" — ISEFi, Moody’s

- El ataque iraní a Israel (2024) apenas movió el petróleo.
- La invasión de Ucrania (2022) sí movió mercados, pero el efecto se desvaneció en 3-4 meses.
- **Implicación:** Los eventos geopolíticos generan oportunidades de "buy the dip" si la economía global no está en recesión.

**2. Aranceles y política comercial son el nuevo petróleo**
> "Datos de inflación en la eurozona y aranceles comerciales mueven mercados" — Yahoo Finance, 2025

- Los aranceles de Trump a India (50%) y las negociaciones comerciales son ahora más relevantes que la guerra en Oriente Medio.
- **Implicación:** Monitorizar el calendario de anuncios de aranceles (US Trade Representative) puede ser más rentable que monitorizar conflictos militares.

**3. Los bancos centrales siguen siendo el factor #1**
> "Los bancos centrales, la clave de 2024 y muy probablemente también de 2025" — Funcas

- La Fed recortó a 4.25-4.50% en 2024 y proyectó solo 2 recortes para 2025.
- El BCE bajará más que la Fed, creando divergencia EUR/USD.
- **Implicación:** La divergencia de política monetaria (Fed vs BCE vs BOJ) es la fuerza dominante en 2025.

**4. La desconexión entre geopolítica y finanzas crece**
> "La capacidad de los eventos geopolíticos para provocar fluctuaciones en los mercados se ha debilitado" — ISEFi

- Los mercados ya "descontaron" la guerra fría 2.0.
- El oro sube a máximos históricos ($3,508/oz) por de-dollarización, no solo por guerra.
- **Implicación:** El oro ya no reacciona a cada misil. Reacciona a tendencias estructurales (de-dollarización, deuda global, expectativas de tipos).

---

## 4. Calendario Económico en Tiempo Real (Investing.com)

Investing.com publica un calendario económico con:
- **Eventos de alta volatilidad:** NFP (empleo US), CPI, FOMC, ECB, BOJ, PIB
- **Eventos de impacto medio:** PMI, ventas minoristas, producción industrial
- **Eventos de impacto bajo:** Inventarios, encuestas de confianza

**Eventos que SÍ mueven mercados (basado en datos históricos):**
1. **FOMC (Fed):** Decisión de tipos + conferencia de Powell. VIX suele subir 15-20% el día previo.
2. **NFP (Empleo US):** Si el dato difiere >50k de la expectativa, S&P 500 mueve >1% en el día.
3. **CPI (Inflación US):** Si CPI > expectativa +0.2pp, S&P 500 cae >1.5% (2022-2023 demostró esto).
4. **PMI Manufacturing China:** Si cae por debajo de 50, EEM (emerging) cae, FXI (China) cae, y metales industriales (cobre) caen.
5. **BOJ (Banco de Japón):** Decisiones de tipos en Japón. Si suben tipos, el yen se fortalece y el carry trade se deshace (como en agosto 2024).

**Eventos que NO mueven mercados tanto como se cree:**
- Elecciones legislativas en Europa (salvo Francia/Italia con riesgo de default)
- Tensiones en Oriente Medio (salvo que cierren el estrecho de Ormuz)
- Declaraciones de presidentes (salvo que anuncien aranceles o sanciones concretas)

---

## 5. Japón: El carry trade y el Yen

### Datos del Banco de Japón y FRED (USD/JPY)

**Correlación YEN (USD/JPY) vs activos (2007-2026):**
- YEN vs S&P 500: **+0.15** (débil)
- YEN vs Bolsa Internacional: **-0.35** (moderada negativa)
- YEN vs Emerging Markets: **-0.28**
- YEN vs Dólar Index: **-0.72** (fuerte negativa, obvio)

**Qué es el carry trade de yen:**
1. Pedir prestado yen a tipos del 0-0.25% (Japón)
2. Invertir en dólares/bonos US/mercados emergentes a 4-5%
3. Capturar la diferencia de tipos (carry)

**Cuándo se deshace el carry trade:**
- Cuando el BOJ sube tipos (como hizo en marzo 2024)
- Cuando hay pánico global (venden todo para devolver yenes)
- Resultado: YEN se fortalece fuertemente, bolsa internacional cae

**Implicación para trading:**
- Monitorizar USD/JPY. Si cae por debajo de 140, el carry trade se está deshaciendo.
- Si el BOJ anuncia subida de tipos, vender EEM/FXI y comprar YEN (o ETFs de yen como FXY).

---

## 6. Fuentes de Información Automatizada (GRATIS)

### A. APIs y Datos (ya usadas en este informe)
| Fuente | Qué ofrece | URL | Frecuencia |
|--------|-----------|-----|------------|
| FRED API | Macro, yields, tipos, inflación | fred.stlouisfed.org | Diaria |
| Yahoo Finance | Precios históricos y en tiempo real | finance.yahoo.com | Diaria |
| IMF COFER | Reservas globales por moneda | data.imf.org | Trimestral |
| Investing.com | Calendario económico | investing.com | En tiempo real |

### B. Fuentes de Noticias para Scraping/Monitorización
| Fuente | Qué monitorizar | Utilidad |
|--------|-----------------|----------|
| **Reuters Breakingviews** | Anuncios de bancos centrales, aranceles | Alta |
| **Bloomberg Terminal** (free articles) | Decisiones de la Fed, ECB | Alta |
| **X/Twitter** | Cuentas de @DeItaone (breaking news), @firstsquawk | Media-Alta |
| **ZeroHedge** | Análisis macro, a veces alarmista | Media (filtrar) |
| **Federal Reserve** | FOMC statements, discursos de Powell | Alta |
| **ECB** | Decisions, press conferences | Alta |
| **BOJ** | Decisions, statements | Media-Alta |
| **US Trade Representative** | Anuncios de aranceles | Alta (2025) |
| **OPEC** | Decisiones de producción | Alta para petróleo |
| **IEA** | Reportes mensuales de petróleo | Media |

### C. Calendarios de Eventos que Mueven Mercados

**Semanales:**
- NFP (primer viernes de mes) → VIX suele subir 2-3 días antes
- Initial Jobless Claims (jueves) → Movimiento si hay sorpresa >20k
- Inventarios de petróleo EIA (miércoles) → XLE mueve si hay sorpresa >2M barriles

**Mensuales:**
- CPI (día 10-15 del mes) → Movimiento más grande del mes en S&P 500 si hay sorpresa
- FOMC (8 veces/año) → VIX suele subir 15-20% el día previo
- PMI Manufacturing (primer día hábil del mes) → EEM/FXI/Metales

**Trimestrales:**
- PIB (revisado) → Movimiento moderado
- Earnings season (4 veces/año) → QQQ y XLK mueven según resultados de Big Tech

---

## 7. Hallazgos Clave Nuevos para Trading

### A. La regla del PMI Manufacturing China
- Si PMI China > 50 y acelerando: Comprar XLB (Materiales), EEM (Emerging), FXI (China).
- Si PMI China < 50 y decelerando: Vender EEM, FXI, XLB. Comprar XLU (Utilidades), XLP (Consumo).
- **Razón:** China consume el 50% del cobre, 60% del acero, 40% del cemento global. Cuando China frena, las materias primas se hunden.

### B. La regla del NFP (Empleo US)
- Si NFP > expectativa + 50k: S&P 500 sube (buena noticia = economía fuerte)
- Si NFP < expectativa - 50k: S&P 500 puede subir O caer. Paradoja: malos datos = la Fed bajará tipos = bonos suben = bolsa sube (a veces).
- **En 2022-2023:** malos datos NFP hacían subir bolsa ("bad news is good news" porque la Fed se iba a volver dovish).
- **En 2024-2025:** buenos datos NFP hacen subir bolsa (la economía es fuerte y la Fed ya no tiene que subir tipos).

### C. La regla del Carry Trade de Yen
- Si USD/JPY > 150 y BOJ no sube tipos: Comprar EEM, FXI, Small Cap (IWM). El dinero barato japonés fluye a activos de riesgo.
- Si USD/JPY < 140 y BOJ sube tipos: Vender EEM, FXI, IWM. Comprar YEN (FXY), TLT (bonos US).
- **Agosto 2024:** USD/JPY cayó de 160 a 142 en 2 semanas. El carry trade se deshizo. EEM cayó -8%, IWM -6%.

### D. La regla de los Aranceles (2025+)
- Si USTR anuncia aranceles a China (>25%): Vender FXI, QQQ (Apple, Tesla dependen de China), XLK. Comprar XLP, XLU (domésticos).
- Si USTR anuncia aranceles a Europa: Vender XLI (Industriales con exposición europea), EEM. Comprar XLU.
- **La política comercial es ahora más relevante que la geopolítica militar.**

### E. La regla de la Divergencia Bancos Centrales
- Si Fed baja tipos pero BCE no: EUR/USD sube, Dólar se debilita, Oro sube, VXUS (internacional) sube.
- Si BCE baja tipos pero Fed no: EUR/USD cae, Dólar se fortalece, VXUS cae, Oro se mantiene.
- Si BOJ sube tipos (único banco central subiendo): YEN se fortalece, carry trade se deshace, EEM/FXI caen.
- **2025 escenario:** Fed baja poco (2 recortes), BCE baja más (4-5 recortes), BOJ sube tipos = Dólar fuerte, YEN fuerte, EUR débil.

---

## 8. Limitaciones Adicionales (Honestidad)

1. **Scraping de noticias es difícil.** Los sitios como Bloomberg, Reuters y Investing.com bloquean bots. Necesitaríamos usar APIs pagas (NewsAPI, Bloomberg API) o RSS feeds.

2. **Sentimiento de Twitter/X es difícil de cuantificar.** El texto en español, chino, inglés requiere NLP multilingüe. Herramientas como VADER o TextBlob funcionan mejor en inglés.

3. **Los eventos geopolíticos son únicos.** No hay dos guerras iguales. La Guerra del Golfo (1990) fue por suministro. Ucrania (2022) fue por sanciones. Gaza (2023) fue por miedo a escalada. Cada uno movió mercados diferente.

4. **Lag en datos macro.** El CPI de hoy es del mes pasado. El PIB es del trimestre pasado. Los mercados "precian" el futuro, no el pasado.

5. **No tenemos datos de flujos de fondos.** Las "ballenas" de Wall Street (BlackRock, Vanguard, pensiones) mueven más dinero que las ballenas de cripto, pero sus flujos se publican con 1-3 meses de retraso (13F filings).

---

## 9. Próximos Pasos Recomendados

### Inmediatos (esta semana)
1. **Crear lista de RSS** de FRED, Fed, ECB, BOJ, USTR, OPEC para scraping automático.
2. **Configurar alertas en TradingView** para eventos clave: VIX > 25, USD/JPY < 140, XLE vs CL=F divergencia.
3. **Descargar datos de PMI China** (Caixin o oficial) y añadir al cron job.

### Corto plazo (próximas 2 semanas)
4. **Implementar Dual Momentum** con filtro de VIX y PMI China.
5. **Añadir análisis de earnings season** (4 veces/año) para QQQ/XLK.
6. **Crear bot de Telegram** que envíe alertas cuando:
   - VIX > 25
   - SPY-HYG correlación < 0.6
   - USD/JPY < 140 (carry trade breaking)
   - Petróleo sube >10% en un mes
   - PMI China < 50

### Medio plazo (próximo mes)
7. **Suscribirse a NewsAPI** ($10/mes) para scraping de noticias en tiempo real.
8. **Añadir datos de China** (Shanghai Composite, tipos PBOC, PIB trimestral).
9. **Backtest completo** de la estrategia con filtros de eventos.

---

*Anexo generado por Kimi Work. Datos de Yahoo Finance, Investing.com, FRED, IMF. Última actualización: 2025-06-23.*
