from enum import Enum

__all__ = "Platform"


class Platform(Enum):
    """Platform names."""

    value: str
    #: UPlay/PC Network
    uplay = "uplay"  # pc
    #: The Playstation Network
    psn = "psn"  # playstation
    #: XBox Live
    xbox = "xbx"  # xbox

    def __str__(self) -> str:
        return self.value
