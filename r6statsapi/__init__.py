from .client import Client as Client
from .enums import Platform as Platform
from .enums import Regions as Regions
from .errors import HTTPException as HTTPException
from .errors import InternalError as InternalError
from .errors import PlayerNotFound as PlayerNotFound
from .errors import R6StatsApiException as R6StatsApiException
from .errors import Unauthorized as Unauthorized
from .player import Gamemodes as Gamemodes
from .player import Leaderboard as Leaderboard
from .player import Operators as Operators
from .player import Player as Player
from .player import Queue as Queue
from .player import Seasonal as Seasonal
from .player import WeaponCategories as WeaponCategories
from .player import Weapons as Weapons

__version__ = "0.1.9"
__author__ = "Jamie (flare)"


__all__ = (
    "Client",
    "Platform",
    "Regions",
    "Player",
    "Queue",
    "Seasonal",
    "Operators",
    "Weapons",
    "WeaponCategories",
    "Gamemodes",
    "Leaderboard",
    "R6StatsApiException",
    "Unauthorized",
    "PlayerNotFound",
    "HTTPException",
    "InternalError",
)
