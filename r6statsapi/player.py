from typing import Dict, List

from .enums import Platform, Regions

__all__ = (
    "Player",
    "Operators",
    "Weapons",
    "Seasonal",
    "WeaponCategories",
    "Gamemodes",
    "Queue",
    "Leaderboard",
)


class Player:
    """ "Player()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    aliases: list
        List of previous user aliases.
    level: int
        Player's level.
    lootbox_probability: int
        Player's probability of getting a lootbox.
    total_xp: int
        Players total XP.
    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")

        # generic
        self.aliases: List = data.get("aliases", [])
        self.progression: Dict = data.get("progression", {})
        self.level: int = self.progression.get("level", 0)
        self.lootbox_probability: int = self.progression.get("lootbox_probability")
        self.total_xp: int = self.progression.get("total_xp")
        self.all_stats: Dict = data.get("stats", {})
        self.general_stats: Dict = self.all_stats.get("general")
        self.queue_stats: Dict = self.all_stats.get("queue")
        self.gamemode_stats: Dict = self.all_stats.get("gamemode")


class Operators:
    """ "Operators()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    operators: dict
        Player's operator stats mapped to a dictionary.

    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")
        self.operators: Dict = data.get("operators", None)


class Weapons:
    """ "Weapons()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    weapons: dict
        Player's weapons stats mapped to a dictionary.

    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")
        self.weapons: Dict = data.get("weapons", None)


class Seasonal:
    """ "Seasonal()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    seasons: dict
        Player's seasonal stats mapped to a dictionary.

    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")
        self.seasons: Dict = data.get("seasons", None)


class WeaponCategories:
    """ "WeaponCategories()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    weapon_categories: dict
        Player's weapon categort stats mapped to a dictionary.

    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")
        self.weapon_categories: Dict = data.get("categories", None)


class Gamemodes:
    """ "Gamemodes()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    bomb: dict
        Player's bomb stats mapped to a dictionary.
    secure_area: dict
        Player's secure area stats mapped to a dictionary.
    hostage: dict
        Player's hostage stats mapped to a dictionary.
    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")
        self.all_stats: Dict = data.get("stats", {})
        self.gamemode_stats: Dict = self.all_stats.get("gamemode")
        self.bomb: Dict = self.gamemode_stats.get("bomb")
        self.secure_area: Dict = self.gamemode_stats.get("secure_area")
        self.hostage: Dict = self.gamemode_stats.get("hostage")


class Queue:
    """ "Queue()
    Represents R6 Player

    Attributes
    ----------
    platform: `Platform`
        Player's platform.
    username: str
        Player's username (display name)
    avatar_url_256: str
        Player's 256x256 Avatar
    avatar_url_146: str
        Player's 146x146 Avatar
    casual: dict
        Player's casual stats mapped to a dictionary.
    ranked: dict
        Player's ranked stats mapped to a dictionary.
    other: dict
        Player's other stats mapped to a dictionary.
    """

    def __init__(self, *, platform: Platform, data: Dict):
        self.name: str = data.get("username", "")
        self.username: str = self.name
        self.platform = platform
        self.avatar_url_256: str = data.get("avatar_url_256", "")
        self.avatar_url_146: str = data.get("avatar_url_146", "")
        self.all_stats: Dict = data.get("stats", {})
        self.queue_stats: Dict = self.all_stats.get("queue")
        self.casual: Dict = self.queue_stats.get("casual")
        self.ranked: Dict = self.queue_stats.get("ranked")
        self.other: Dict = self.queue_stats.get("other")


class Leaderboard:
    """ "Leaderboard`()
    Represents R6 Leaderboard

    Attributes
    ----------
    platform: `Platform`
        Leaderboard platform.
    region: `Regions`
        Leaderboard region
    leaderboard: list
        Leaderboard mapped to a list of dictionarys.
    """

    def __init__(self, *, platform: Platform, region: Regions, data: Dict):
        self.platform = platform
        self.region = region
        self.leaderboard = data
