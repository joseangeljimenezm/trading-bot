from datetime import datetime

import requests

from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_telegram(text: str) -> bool:
    if not TELEGRAM_BOT_TOKEN:
        return False
    chat_id = _resolve_chat_id()
    if not chat_id:
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}, timeout=10)
        return resp.status_code == 200
    except Exception as e:
        print(f"  Telegram error: {e}")
        return False


def send_signal_report(vote: str, confidence: float, regime: str, signals: list, allocation: dict[str, float]):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"*Señales {now}*",
        f"Voto: *{vote.upper()}* | Confianza: {confidence:.0%} | Régimen: {regime}",
        "",
    ]
    for s in signals:
        emoji = {"bullish": "🟢", "bearish": "🔴", "neutral": "⚪"}.get(s.vote.value, "⚪")
        lines.append(f"{emoji} *{s.signal_name}*: {s.details}")
    lines.append("")
    lines.append("*Cartera sugerida:*")
    for ticker, pct in sorted(allocation.items(), key=lambda x: -x[1]):
        lines.append(f"  {ticker}: {pct:.1%}")
    send_telegram("\n".join(lines))


def _resolve_chat_id() -> str | None:
    if TELEGRAM_CHAT_ID:
        return TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data.get("ok") and data.get("result"):
            chat_id = str(data["result"][0]["message"]["chat"]["id"])
            return chat_id
    except Exception:
        pass
    return None
