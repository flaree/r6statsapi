from enum import Enum

__all__ = ("Platform", "Regions")


class Platform(Enum):
    """Platform names."""

    value: str
    #: UPlay/PC Network
    uplay = "uplay"  # pc
    #: The Playstation Network
    psn = "psn"  # playstation
    #: XBox Live
    xbox = "xbl"  # xbox

    xbl = xbox
    ps4 = psn
    pc = uplay

    def __str__(self) -> str:
        return self.value


class Regions(Enum):
    """R6Stats Regions."""

    value: str
    #: All Regions
    all = "all"
    #: North America
    ncsa = "ncsa"
    #: Europe
    emea = "emea"
    #: Asia
    apac = "apac"

    eu = emea
    na = ncsa
    asia = apac

    def __str__(self) -> str:
        return self.value
