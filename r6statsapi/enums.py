from enum import Enum

__all__ = "Platform"


class Platform(Enum):
    """Platform names."""

    value: str
    uplay = "uplay"  # pc
    psn = "psn"  # playstation
    xbox = "xbx"  # xbox

    def __str__(self) -> str:
        return self.value
