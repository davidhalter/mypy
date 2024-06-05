from typing import Iterable, Tuple


# --zuban-diff def ex(a):
# --zuban-diff     # type: (Iterable[str]) -> Tuple[str, ...]
def ex(a: Iterable[str]) -> Tuple[str, ...]:
    """Example typed package."""
    return list(a)
