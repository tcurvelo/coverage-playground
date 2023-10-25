from datetime import datetime

import dateparser

settings = {"TIMEZONE": "UTC", "TO_TIMEZONE": "UTC"}


def get_time(prompt) -> datetime:
    dt = dateparser.parse(prompt, settings=settings)
    if not dt:
        raise ValueError("Invalid date")
    return dt
