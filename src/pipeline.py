"""Pipeline principal: escáner de oportunidades + órdenes."""

from src.scanner import run_scan
from src.tracker import open_positions
from src.ibkr import generate_orders, format_orders_text
from src.notifications import send_telegram


def run_pipeline(save_to_db: bool = True, notify: bool = True):
    scan = run_scan()
    orders = generate_orders(scan.positions)

    print(scan.summary)
    print()
    print(format_orders_text(orders))

    if save_to_db:
        open_positions(scan.positions, scan.regime)

    if notify:
        full_msg = scan.summary + "\n\n" + format_orders_text(orders)
        if len(full_msg) > 4000:
            send_telegram(scan.summary)
            send_telegram(format_orders_text(orders))
        else:
            send_telegram(full_msg)
        print(f"\n  Telegram: enviado")


def main():
    run_pipeline()


if __name__ == "__main__":
    main()
