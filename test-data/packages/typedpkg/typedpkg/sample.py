from typing import Iterable, Tuple


# --zuban-diff def ex(a):
# --zuban-diff     # type: (Iterable[str]) -> Tuple[str, ...]
def ex(a: Iterable[str]) -> Tuple[str, ...]:
    """Example typed package."""
# --zuban-diff     return list(a)
    return ()
