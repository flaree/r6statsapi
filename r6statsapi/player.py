from enums import Platform
from typing import Dict, List


class Player:
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

        # seasonal
        self.seasons: Dict = data.get("seasons", None)

        # operators
        self.operators: Dict = data.get("operators", None)

        # weapons
        self.weapons: Dict = data.get("weapons", None)

        # weapon categories
        self.weapon_categories: Dict = data.get("categories", None)
