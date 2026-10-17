"""Current date and time tool using the machine's local timezone."""
from __future__ import annotations

from datetime import datetime


def current_datetime() -> str:
    """Return a readable current timestamp in the machine's local timezone."""
    now = datetime.now().astimezone()
    offset = now.strftime("%z")
    return f"{now.strftime('%A, %B %d, %Y %H:%M:%S %Z')} (UTC{offset[:3]}:{offset[3:]})"
