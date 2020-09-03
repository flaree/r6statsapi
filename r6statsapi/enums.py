from enum import Enum

__all__ = ("Platform", "Regions")


class Platform(Enum):
    """Platform names.

    .. container:: operations
        ``str(x)``
            Returns platform's friendly name, e.g. "Xbox Live"
    """

    value: str
    #: UPlay/PC Network
    uplay = "UPLAY"  # pc

    #: The Playstation Network
    psn = "PSN"  # playstation

    #: Xbox Live
    xbox = "XBL"  # xbox

    #: Alias of xbox
    xbl = xbox

    #: Alias of psn
    ps4 = psn

    #: Alias of uplay
    pc = uplay

    def __str__(self) -> str:
        return self.value


class Regions(Enum):
    """R6Stats Regions.

    .. container:: operations
        ``str(x)``
            Returns platform's friendly name, e.g. "Xbox Live"
    """

    value: str
    #: All Regions
    all = "All Regions"

    #: North America
    ncsa = "North America"

    #: Europe
    emea = "Europe"

    #: Asia
    apac = "Asia"

    #: Alias of emea
    eu = emea
    #: Alias of ncsa
    na = ncsa
    #: Alias of asia
    asia = apac

    def __str__(self) -> str:
        return self.value
