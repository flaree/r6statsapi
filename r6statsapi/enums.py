from enum import Enum

__all__ = ("Platform", "Regions")


class Platform(Enum):
    """Platform names."""

    value: str
    #: UPlay/PC Network
    uplay = "uplay"  # pc
    #: The Playstation Network
    psn = "psn"  # playstation
    #: Xbox Live
    xbox = "xbl"  # xbox

    #: Alias of xbox
    xbl = xbox
    #: Alias of psn
    ps4 = psn
    #: Alias of uplay
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

    #: Alias of emea
    eu = emea
    #: Alias of ncsa
    na = ncsa
    #: Alias of asia
    asia = apac

    def __str__(self) -> str:
        return self.value
