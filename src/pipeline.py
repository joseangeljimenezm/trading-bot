"""Pipeline principal: escáner de oportunidades completo."""

from src.scanner import run_scan
from src.tracker import open_positions
from src.notifications import send_telegram


def run_pipeline(save_to_db: bool = True, send_telegram: bool = True):
    scan = run_scan()

    print(scan.summary)

    if save_to_db:
        open_positions(scan.positions, scan.regime)

    if send_telegram:
        ok = send_telegram(scan.summary)
        print(f"\n  Telegram: {'enviado' if ok else 'fallo'}")


def main():
    run_pipeline()


if __name__ == "__main__":
    main()
