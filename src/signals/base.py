from dataclasses import dataclass
from datetime import date

from src.models.enums import SignalVote


@dataclass
class SignalResult:
    signal_name: str
    vote: SignalVote
    weight: float
    details: str | None = None
