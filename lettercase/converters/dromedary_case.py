from collections import deque
from typing import Deque

__all__ = ["snake_to_dromedary_case"]


def snake_to_dromedary_case(text: str) -> str:
    """Convert from snake_case to dromedaryCase."""
    if not text:
        return text

    chars: Deque[str] = deque()
    next_is_upper: bool = False
    letter_seen: bool = False

    for c in text:
        if c == "_":
            if letter_seen:
                next_is_upper = True
                continue
        elif c.isalpha():
            letter_seen = True

            if next_is_upper:
                c = c.upper()
                next_is_upper = False

        chars.append(c)

    return "".join(chars)
