from enum import Enum

__all__ = ("Platform", "Regions")


class Platform(Enum):
    """Platform names.
    
    """

    value: str
    #: UPlay/PC Network
    uplay = "PC"  # pc

    #: The Playstation Network
    psn = "Playstation Network"  # playstation

    #: Xbox Live
    xbox = "Xbox Live"  # xbox

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
