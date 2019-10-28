from .client import Client as Client
from .enums import Platform as Platform
from .enums import Regions as Regions
from .player import Player as Player
from .player import Queue as Queue
from .player import Seasonal as Seasonal
from .player import Operators as Operators
from .player import Weapons as Weapons
from .player import WeaponCategories as WeaponCategories
from .player import Gamemodes as Gamemodes
from .player import Leaderboard as Leaderboard
from .errors import R6StatsApiException as R6StatsApiException
from .errors import Unauthorized as Unauthorized

__version__ = "0.1.5"
