"""Módulo de conexión IBKR para paper trading.

REQUISITOS para modo real:
  1. Tener IB Gateway o TWS abierto con conexión a paper trading
  2. Configurar en IB Gateway: Edit → Configuration → API → Enable ActiveX and Socket Clients
  3. Marcar "Trusted IP Addresses" con 127.0.0.1
  4. Puerto por defecto: 7497 (paper), 7496 (live)

MODO SIMULADO (por defecto): genera órdenes como texto.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.config import IBKR_PORT, IBKR_HOST, IBKR_CLIENT_ID, IBKR_PAPER
from src.risk import PositionPlan, PORTFOLIO_VIRTUAL


@dataclass
class Order:
    ticker: str
    action: str  # BUY o SELL
    quantity: int
    order_type: str  # MKT, LMT, STP
    limit_price: Optional[float] = None
    stop_price: Optional[float] = None
    ibkr_contract: Optional[str] = None
    reason: str = ""


def generate_orders(positions: list[PositionPlan]) -> list[Order]:
    """Genera órdenes de compra simuladas."""
    orders = []
    for p in positions:
        orders.append(Order(
            ticker=p.ticker,
            action="BUY",
            quantity=p.quantity,
            order_type="MKT",
            reason=f"Asignación {p.target_pct:.0%} cartera RISK ON",
        ))
        orders.append(Order(
            ticker=p.ticker,
            action="SELL",
            quantity=p.quantity,
            order_type="STP",
            stop_price=p.stop_loss,
            reason=f"Stop-loss -10% automático",
        ))
    return orders


def format_orders_text(orders: list[Order]) -> str:
    """Devuelve órdenes como texto legible para copiar a IBKR."""
    lines = [
        f"ORDENES GENERADAS — {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        f"Capital: ${PORTFOLIO_VIRTUAL:,.0f}",
        f"{'=' * 55}",
        f"{'Acción':6s} {'Ticker':6s} {'Cantidad':10s} {'Tipo':6s} {'Precio':10s} {'Motivo'}",
        f"{'-' * 55}",
    ]
    for o in orders:
        price = ""
        if o.limit_price:
            price = f"${o.limit_price:.2f}"
        elif o.stop_price:
            price = f"${o.stop_price:.2f}"
        lines.append(f"{o.action:6s} {o.ticker:6s} {o.quantity:10d} {o.order_type:6s} {price:10s} {o.reason}")

    lines.append(f"{'=' * 55}")
    buy_count = sum(1 for o in orders if o.action == "BUY")
    sell_count = sum(1 for o in orders if o.action == "SELL")
    lines.append(f"Total: {buy_count} compras, {sell_count} stops")
    return "\n".join(f"  {l}" for l in lines)


def connect_ibkr():
    """Intenta conectar con IB Gateway. Solo si está abierto."""
    try:
        from ib_insync import IB
        ib = IB()
        ib.connect(IBKR_HOST, IBKR_PORT, clientId=IBKR_CLIENT_ID)
        print(f"  Conectado a IBKR ({'paper' if IBKR_PAPER else 'live'})")
        return ib
    except ConnectionRefusedError:
        print("  IBKR: Gateway no disponible. Usar modo simulado.")
        return None
    except Exception as e:
        print(f"  IBKR error: {e}")
        return None


def place_orders_via_api(ib, orders: list[Order]) -> list:
    """Coloca órdenes reales via API IBKR. Requiere Gateway abierto."""
    from ib_insync import Stock, MarketOrder, StopOrder
    results = []
    for o in orders:
        contract = Stock(o.ticker, "SMART", "USD")
        if o.order_type == "MKT":
            ib_order = MarketOrder(o.action, o.quantity)
        elif o.order_type == "STP":
            ib_order = StopOrder(o.action, o.quantity, o.stop_price)
        else:
            continue
        trade = ib.placeOrder(contract, ib_order)
        results.append(trade)
    return results
