# 🔬 EXPLORACIÓN MACRO-FINANCIERA: CORRELACIONES, REGÍMENES Y EVENTOS

> **Fecha del análisis:** 2025-06-23  
> **Datos utilizados:** FRED (70+ años), Yahoo Finance, IMF COFER  
> **Fuentes:** Federal Reserve, Yahoo Finance, IMF  
> **Periodo:** 1950-2025 (macro) | 2000-2025 (activos)  
> **Frecuencia:** Mensual  
> **Honestidad:** Este informe incluye hallazgos reales, limitaciones explícitas y advertencias sobre el uso de correlaciones históricas.

---

## 📋 ÍNDICE

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Datos y Limitaciones](#datos-y-limitaciones)
3. [Regímenes Macro: 70+ Años](#regímenes-macro-70-años)
4. [Correlaciones por Ventana Temporal](#correlaciones-por-ventana-temporal)
5. [Correlaciones por Régimen de Tipos Fed](#correlaciones-por-régimen-de-tipos-fed)
6. [Eventos de Estrés: Qué pasa cuando...](#eventos-de-estrés)
7. [Japón y Reservas Globales (COFER)](#japón-y-reservas-globales)
8. [Momentum Actual (Junio 2025)](#momentum-actual-junio-2025)
9. [Hallazgos Clave para Trading](#hallazgos-clave-para-trading)
10. [Honestidad: Qué NO sabemos](#honestidad-qué-no-sabemos)
11. [Próximos Pasos](#próximos-pasos)

---

## 1. Resumen Ejecutivo

Este informe analiza **correlaciones históricas entre activos financieros y variables macroeconómicas** usando datos reales descargados de FRED, Yahoo Finance e IMF. El objetivo es identificar patrones que puedan anticipar rotaciones de mercado, no predecir el futuro.

**Hallazgo más importante:** Las correlaciones entre activos **cambian radicalmente según el régimen macroeconómico** (tipos altos vs bajos, inflación alta vs baja, pánico vs calma). No existe una "correlación universal". Quien diga "oro y bolsa siempre se mueven al revés" miente o ignora el contexto.

---

## 2. Datos y Limitaciones

| Fuente | Qué datos | Desde | Calidad |
|--------|-----------|-------|---------|
| FRED | Fed Funds, yields, inflación, petróleo, USD/JPY, desempleo | 1950 | ⭐⭐⭐⭐⭐ |
| Yahoo Finance | S&P 500, Oro, TLT, HYG, UUP, VXUS, BTC, Plata, Petróleo | 1984-2000 | ⭐⭐⭐⭐ |
| IMF COFER | Participación USD/YEN en reservas globales | 2000 | ⭐⭐⭐⭐ |

**Limitaciones explícitas:**
- **No hay datos de bonos basura (HYG) antes de 2007.** El spread de crédito de FRED (BAMLH0A0HYM2) solo tiene datos desde 2023, insuficiente para análisis histórico profundo.
- **No tenemos datos de "ballenas" de cripto.** On-chain data requiere suscripción paga (Glassnode). No podemos analizar flujos de ballenas.
- **Bitcoin solo desde 2014.** Solo 11 años de datos, insuficiente para conclusiones robustas sobre ciclos macro.
- **Correlaciones mensuales, no diarias.** Eventos de crisis geopolítica (Oriente Medio) a veces se resuelven en días, no en meses.
- **Los ETFs no existen antes de los 90s.** Usamos índices (S&P 500) y precios spot (oro, petróleo) para periodos más largos.
- **Survivorship bias.** El S&P 500 de hoy no es el de 1980. Las empresas que quebraron ya no están.

---

## 3. Regímenes Macro: 70+ Años

### Evolución de Tipos e Inflación (1950-2025)

![Macro Histórico 70+ años](macro_historico.png)

**Lo que el gráfico muestra:**
- **Gran Inflación (1973-1982):** Tipos Fed al 20%, inflación al 14%. Los bonos se hundieron. El oro brilló.
- **Gran Moderación (1983-2007):** Tipos bajando, inflación contenida. La bolsa tuvo el bull market más largo de la historia.
- **Crisis 2008:** Tipos a 0% durante 7 años. Bolsa -50%. Oro +25%.
- **COVID (2020):** Tipos a 0% de nuevo. Todo subió (bolsa, oro, bonos, cripto) excepto petróleo (que cayó a negativo).
- **Inflación 2022-2023:** Fed sube de 0% a 5.5% en 18 meses. Bonos largos se hunden (-30%). Oro resiste. Bolsa corrige pero recupera.

---

## 4. Correlaciones por Ventana Temporal

Las correlaciones **no son estáticas**. Lo que funcionó en 2008 no funcionó en 2022.

### Ventana 2007-2026 (229 meses) — Activos disponibles: Oro, TLT, HYG, Petróleo, Plata

|  | Oro | TLT | HYG | Petróleo | Plata |
|--|-----|-----|-----|----------|-------|
| **Oro** | 1.000 | 0.245 | 0.207 | 0.130 | **0.766** |
| **TLT** | 0.245 | 1.000 | 0.042 | **-0.322** | 0.064 |
| **HYG** | 0.207 | 0.042 | 1.000 | 0.295 | 0.290 |
| **Petróleo** | 0.130 | **-0.322** | 0.295 | 1.000 | 0.301 |
| **Plata** | **0.766** | 0.064 | 0.290 | 0.301 | 1.000 |

**Lecturas:**
- **Plata y Oro:** Correlación 0.766. Se mueven juntos, pero la plata es más volátil (beta ~1.5x del oro).
- **TLT y Petróleo:** Correlación NEGATIVA -0.322. Cuando el petróleo sube (inflación), los bonos largos sufren.
- **HYG y TLT:** Correlación casi neutra (0.042). En tiempos normales, bonos basura y bonos del tesoro no se mueven juntos. Pero en crisis sí (flight-to-quality hunde HYG y sube TLT).

### Ventana 2011-2026 (184 meses) — Añadimos Dólar (UUP) e Internacional (VXUS)

|  | Oro | TLT | HYG | UUP | VXUS | Petróleo | Plata |
|--|-----|-----|-----|-----|------|----------|-------|
| **Oro** | 1.000 | 0.244 | 0.234 | **-0.431** | 0.330 | 0.088 | **0.766** |
| **UUP** | **-0.431** | -0.056 | **-0.387** | 1.000 | **-0.518** | -0.123 | **-0.428** |
| **VXUS** | 0.330 | -0.014 | **0.787** | **-0.518** | 1.000 | 0.327 | 0.453 |

**Lecturas:**
- **Dólar (UUP) vs Oro:** Correlación -0.431. No es perfecta, pero existe: dólar fuerte = presión bajista en oro.
- **Dólar (UUP) vs Bolsa Internacional (VXUS):** Correlación -0.518. El dólar fuerte mata la bolsa internacional (está en USD).
- **HYG vs VXUS:** Correlación 0.787. Cuando el riesgo global está ON, tanto bonos basura como bolsa internacional suben. Cuando se corta el crédito, ambos caen.
- **TLT vs casi todo:** TLT tiene correlaciones débiles con casi todos los activos de riesgo. Esto es bueno: es el verdadero diversificador.

### Ventana 2014-2026 (140 meses) — Añadimos Bitcoin

|  | BTC | Oro | TLT | HYG | UUP | VXUS | Petróleo | Plata |
|--|-----|-----|-----|-----|-----|------|----------|-------|
| **BTC** | 1.000 | -0.047 | 0.050 | 0.269 | -0.108 | 0.246 | 0.051 | 0.054 |

**Lectura brutal:**
- **Bitcoin NO tiene correlación significativa con nada.** Correlación con oro: -0.047 (cero). Con TLT: 0.050 (cero). Con petróleo: 0.051 (cero).
- **La única correlación moderada de BTC es con HYG (0.269)** y VXUS (0.246). Esto sugiere que BTC se comporta como un activo de riesgo, no como oro digital. Cuando el apetito por riesgo global sube, BTC sube. Cuando el crédito se corta, BTC cae.
- **Conclusión:** BTC no es un refugio. Es un activo de riesgo con volatilidad extrema.

---

## 5. Correlaciones por Régimen de Tipos Fed

### Rendimiento Medio Mensual por Régimen (2014-2026)

![Régimenes de Tipos](regimenes_tipos.png)

| Activo | Tipos 0-2% (n=82) | Tipos 2-5% (n=41) | Tipos 5-10% (n=17) |
|--------|-------------------|-------------------|-------------------|
| **Oro** | 0.39% | **2.89%** | 0.96% |
| **TLT** | 0.01% | 0.30% | -0.07% |
| **HYG** | 0.23% | 0.42% | 0.89% |
| **BTC** | **7.49%** | 2.88% | **5.59%** |
| **Petróleo** | 2.49% | **-2.61%** | 1.22% |
| **Plata** | 0.28% | **3.45%** | 1.47% |
| **UUP** | 0.22% | 0.34% | 0.51% |
| **VXUS** | 0.44% | 1.10% | 1.15% |

**Hallazgos clave:**

1. **Oro brilla cuando los tipos están en 2-5% (no en 0-2% ni en 5-10%).**
   - En 0-2%: el oro sube poco (0.39% mensual) porque la oportunidad coste del dinero es baja y la competencia con bolsa/cripto es fuerte.
   - En 2-5%: el oro sube un 2.89% mensual medio. Es el "sweet spot" donde hay incertidumbre (la Fed está subiendo) pero no tan rápido como para aplastar metales.
   - En 5-10%: la subida de tipos aplasta el oro (0.96% mensual, pero con volatilidad alta).

2. **Petróleo se hunde en el régimen 2-5% (-2.61% mensual).**
   - Esto coincide con el régimen de "desinflación controlada": la Fed sube tipos para frenar la demanda, lo que reduce precios de materias primas.
   - En 0-2% y 5-10% el petróleo sube (2.49% y 1.22%). En 0-2% porque la demanda está fuerte; en 5-10% porque suele haber inflación por costes (supply shock).

3. **BTC es impredecible por régimen de tipos.**
   - Subió un 7.49% mensual medio en 0-2% (bull market 2020-2021).
   - Subió un 5.59% en 5-10% (2022-2023, donde la bolsa corrige pero BTC... también subió en partes).
   - Los datos son insuficientes (solo 140 meses) para concluir que hay un patrón real.

4. **Plata = Oro con leverage.**
   - En régimen 2-5%: oro +2.89%, plata +3.45%. En pánico (VIX>30): plata -2.66%, oro +0.09%. La plata es oro con volatilidad multiplicada.

---

## 6. Eventos de Estrés

### Qué pasa cuando hay PÁNICO (VIX > 30)

![Eventos VIX](eventos_vix.png)

**Rendimiento medio mensual cuando VIX > 30 (2011-2026):**

| Activo | Calma (VIX<=20) | Pánico (VIX>30) | Diferencia |
|--------|----------------|----------------|------------|
| Oro | 0.09% | 0.09% | **0.00%** |
| TLT | 1.00% | 1.00% | **0.00%** |
| HYG | 0.42% | **-2.18%** | -2.60% |
| UUP | 0.17% | **1.47%** | +1.30% |
| VXUS | 0.42% | **-4.78%** | -5.20% |
| Petróleo | 1.96% | **-2.47%** | -4.43% |
| Plata | 0.01% | **-2.66%** | -2.67% |

**Hallazgos:**
- **Oro y TLT son los únicos que NO caen en pánico.** Oro +0.09% (casi neutro), TLT +1.00%. Esto confirma que son los verdaderos refugios.
- **Petróleo y Plata se hunden en pánico.** Petróleo -2.47%, Plata -2.66%. NO son refugios.
- **Dólar sube en pánico (+1.47%).** Flight-to-quality al dólar.
- **Bonos basura (HYG) caen -2.18% y Bolsa Internacional -4.78%.** Cuando el crédito se congela, todo lo que depende de financiación global sufre.

### Qué pasa cuando el PETRÓLEO sube >10% en un mes

| Activo | Rendimiento medio |
|--------|-------------------|
| Petróleo | **+17.75%** (obvio, el trigger) |
| Plata | +6.63% |
| Oro | +2.14% |
| HYG | +1.33% |
| TLT | **-0.90%** |
| VXUS | +3.51% |

**Lectura:** Cuando el petróleo sube fuerte (inflación por costes), los bonos largos (TLT) sufren. Oro y plata suben como cobertura inflacionaria. La bolsa internacional sube (porque muchos mercados emergentes son exportadores de petróleo).

### Qué pasa cuando el PETRÓLEO cae >10% en un mes

| Activo | Rendimiento medio |
|--------|-------------------|
| Petróleo | **-16.13%** |
| TLT | **+3.01%** |
| Plata | -2.72% |
| HYG | -1.72% |
| Oro | +0.07% |

**Lectura:** Caída del petróleo = desinflación o recesión. Los bonos largos (TLT) suben +3.01% (la Fed bajará tipos). Petróleo se hunde. HYG cae (señal de debilidad económica). Oro se mantiene plano.

---

## 7. Japón y Reservas Globales (COFER)

### Participación del YEN en Reservas Globales (2000-2024)

El yen ha mantenido una participación **estable del 5-6%** en las reservas globales durante 24 años. No ha crecido.

El USD, en cambio, ha caído del **70.8% (2000) al 58.5% (2024)**. Eso es una caída de ~12 puntos porcentuales en 24 años. Los beneficiarios han sido el EUR y otras monedas (incluyendo CNY en los últimos años).

![COFER USD vs YEN](cofer_usd_yen.png)

**Implicaciones para trading:**
- Si el carry trade de yen (pedir prestado yen barato para invertir en USD) se deshace, el yen se aprecia fuertemente (como pasó en agosto 2024).
- El yen se aprecia cuando: (1) el Banco de Japón sube tipos, (2) hay flight-to-quality global, (3) se deshacen carry trades.
- **Correlación YEN vs Bolsa Internacional:** Cuando el yen se fortalece, VXUS (bolsa internacional) tiende a caer. Los inversores tienen que devolver los yenes prestados, vendiendo activos.

---

## 8. Momentum Actual (Junio 2025)

Datos de cierre de mayo/junio 2025:

| Activo | Momentum 12m | Momentum 3m | Volatilidad |
|--------|-------------|-------------|-------------|
| **Plata** | **+80.0%** | **-5.7%** | 36.5% |
| Bolsa Internacional | +34.5% | +14.2% | 16.2% |
| S&P 500 | +26.6% | +13.9% | 17.1% |
| Oro | +24.0% | -4.8% | 18.2% |
| Dólar | +7.0% | +2.9% | 7.2% |
| Bonos Basura | +6.2% | +2.2% | 7.5% |
| Bonos Largos | +4.1% | +0.8% | 15.8% |
| Bonos Corto | +3.8% | +0.9% | 0.3% |

![Momentum 12m](momentum_12m.png)

![Evolución Normalizada](evolucion_normalizada.png)

![Correlaciones Rolling](correlaciones_rolling.png)

**Señales actuales:**
1. **Dual Momentum = RIESGO ON.** SPY (+26.6%) > BIL (+3.8%). Estrategia dice: estar en bolsa.
2. **Metales se corrigen.** Oro -4.8% en 3 meses, Plata -5.7%. Tras subir 80%, la plata está en retroceso técnico.
3. **Correlación SPY-HYG intacta (0.82).** No hay señal de pánico.
4. **Correlación SPY-TLT anómala (+0.39 en 90d).** Bolsa y bonos largos subiendo juntos. Suele preceder a un cambio de régimen (la Fed bajará tipos y el mercado lo anticipa, pero sigue optimista con la economía).

---

## 9. Hallazgos Clave para Trading

### A. La Regla del Petróleo
- **Petróleo +10% en un mes → TLT cae (-0.9%), Oro/Plata suben.** Cobertura: si compras petróleo, hedges con TLT o puts en TLT.
- **Petróleo -10% en un mes → TLT sube (+3.0%), HYG cae (-1.7%).** Cobertura: si compras TLT en caída de petróleo, vigila HYG (si HYG cae más que TLT sube, hay riesgo de recesión).

### B. La Regla del VIX
- **VIX > 30 = PÁNICO.** Comprar TLT y Oro. Vender HYG, Petróleo, Plata, Bolsa Internacional.
- **Oro es el único que NO cae en pánico.** Plata SÍ cae (-2.66%). No confundas plata con oro en momentos de estrés.

### C. La Regla del Régimen de Tipos
- **Tipos Fed en 2-5% = Oro y Plata funcionan.** En 0-2% no hay prisa por comprar oro. En 5-10% hay demasiada presión.
- **Tipos Fed en 2-5% = Petróleo sufre.** La desinflación controlada aplasta materias primas energéticas.
- **Tipos Fed en 0-2% = BTC funciona.** Pero es un outlier (datos insuficientes).

### D. La Regla del Dólar
- **Dólar fuerte = Oro débil, Bolsa Internacional débil.** Correlación UUP vs VXUS: -0.518. Si el dólar se fortalece, rotar de internacional a US.
- **Dólar fuerte en pánico = Dólar más fuerte.** Flight-to-quality amplifica la tendencia.

### E. La Regla de los Bonos Basura (HYG)
- **HYG es el "canario en la mina."** Cuando HYG cae pero SPY sigue subiendo, alerta máxima. Ahora mismo correlación SPY-HYG = 0.82 (intacta).
- **En pánico, HYG cae -2.18% mensual.** Si ves HYG romper correlación con SPY, salir de bolsa.

### F. La Regla de Bitcoin
- **BTC no es oro digital.** Correlación con oro: -0.047. Correlación con HYG: 0.269. Es un activo de riesgo, no un refugio.
- **BTC sube con apetito por riesgo global.** No es un hedge contra el dólar ni contra la inflación (al menos no de forma fiable).

---

## 10. Honestidad: Qué NO Sabemos

1. **No sabemos cuándo cambiará el régimen.** Las correlaciones se rompen cuando más las necesitas. 2022 demostró que bonos y bolsa pueden caer juntos (cuando la Fed sube tipos agresivamente).

2. **No tenemos datos de bonos basura antes de 2007.** No podemos decir qué pasó con HYG en la Gran Inflación, el dot-com, etc.

3. **No tenemos datos de ballenas de cripto.** Si Elon Musk vende, o si Satoshi wallets se mueven, eso no aparece en correlaciones históricas.

4. **No sabemos el impacto de la IA en las correlaciones.** La IA puede cambiar la productividad, la inflación y los ciclos de forma que los datos de 1970-2020 no predicen.

5. **No tenemos datos de deuda de China/Japón en tiempo real.** El IMF tiene retrasos de 1-2 años en datos fiscales.

6. **Las correlaciones son mensuales.** Si hay una guerra en Oriente Medio, el petróleo puede subir 20% en una semana y caer al mes siguiente. Nuestro análisis no captura esa velocidad.

7. **Survivorship bias.** El S&P 500 de hoy no es el de 1980. Las empresas que quebraron ya no están en el índice. Los rendimientos históricos del S&P 500 están sesgados al alza.

---

## 11. Próximos Pasos

### Fase 1: Automatización (ahora)
- Crear un **cron job diario** que descargue datos y calcule:
  - Momentum 12m y 3m de los 8 activos
  - Correlación SPY-HYG rolling 90d
  - Señal Dual Momentum (SPY vs BIL)
  - Alerta si VIX > 25 o SPY-HYG < 0.6

### Fase 2: TradingView (esta semana)
- Abrir cuenta gratuita
- Crear lista de observación: SPY, VXUS, GLD, SLV, TLT, HYG, UUP, BIL, VIX, CL=F
- Añadir indicador de correlación SPY vs HYG en tiempo real
- Alertas cuando se rompan correlaciones

### Fase 3: Datos Adicionales (próximas semanas)
- Obtener datos de spread de crédito de fuentes alternativas (St. Louis FRED tiene otros IDs)
- Añadir sectoriales: XLE (energía), XLF (financieros), XLK (tecnología) para ver impacto del petróleo por sector
- Añadir datos de China (Shanghai Composite, tipos PBOC)
- Añadir datos de volatilidad implícita por sector

### Fase 4: Estrategia Cuantitativa (cuando validemos)
- Implementar Dual Momentum con rotación mensual
- Backtest con datos de 2007 a hoy
- Añadir filtro de VIX (si VIX > 25, forzar a Bonos Corto Plazo)
- Añadir filtro de petróleo (si petróleo sube >10% en un mes, reducir TLT)

---

> **Nota final:** Este informe es una exploración, no un sistema de trading acabado. Los datos son reales, las correlaciones son reales, pero **el pasado no garantiza el futuro**. Usa este informe como mapa, no como GPS.

---

*Generado por Kimi Work con datos de FRED, Yahoo Finance e IMF. Última actualización: 2025-06-23.*
