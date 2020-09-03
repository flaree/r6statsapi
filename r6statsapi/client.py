import asyncio
from typing import Optional

import aiohttp

from . import errors
from .enums import Platform, Regions
from .player import (
    Gamemodes,
    Leaderboard,
    Operators,
    Player,
    Queue,
    Seasonal,
    WeaponCategories,
    Weapons,
)

__all__ = ("Client",)
R6API_BASE = "https://api2.r6stats.com/public-api"


class Client:
    def __init__(self, token: str, *, loop: Optional[asyncio.BaseEventLoop] = None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=self.loop)
        self._headers = {"Authorization": "Bearer {}".format(token)}

    async def _request(self, url: str) -> dict:
        async with self._session.get(url, headers=self._headers) as resp:
            data = await resp.json()
            if resp.status == 200:
                return data
            if resp.status == 401:
                raise errors.Unauthorized()
            if resp.status == 400:
                raise errors.PlayerNotFound()
            if resp.status in [500, 502]:
                raise errors.InternalError()
            raise errors.HTTPException(resp, data)

    def destroy(self) -> None:
        self._session.detach()

    __del__ = destroy

    async def get_generic_stats(self, player: str, platform: Platform) -> Player:
        """
        Get generic player statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.

        Returns
        -------
        Player
            Requested player stats

        """
        endpoint = f"/stats/{player}/{platform}/generic"
        data = await self._request(R6API_BASE + endpoint)
        player = Player(platform=platform, data=data)
        return player

    async def get_seasonal_stats(self, player: str, platform: Platform) -> Seasonal:
        """
        Get seasonal player statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.

        Returns
        -------
        Season
            Requested players seasonal stats
        """
        endpoint = f"/stats/{player}/{platform}/seasonal"
        data = await self._request(R6API_BASE + endpoint)
        seasonal = Seasonal(platform=platform, data=data)
        return seasonal

    async def get_operators_stats(self, player: str, platform: Platform) -> Operators:
        """
        Get a players operator statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.

        Returns
        -------
        Operators
            Requested players operator statistics
        """
        endpoint = f"/stats/{player}/{platform}/operators"
        data = await self._request(R6API_BASE + endpoint)
        operators = Operators(platform=platform, data=data)
        return operators

    async def get_weapon_stats(self, player: str, platform: Platform) -> Weapons:
        """
        Get weapon player statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.

        Returns
        -------
        Weapons
            Requested players weapon stats
        """
        endpoint = f"/stats/{player}/{platform}/weapons"
        data = await self._request(R6API_BASE + endpoint)
        weapons = Weapons(platform=platform, data=data)
        return weapons

    async def get_weaponcategory_stats(self, player: str, platform: Platform) -> WeaponCategories:
        """
        Get a players weapin category statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.

        Returns
        -------
        WeaponCategories
            Requested a players weapon category stats
        """
        endpoint = f"/stats/{player}/{platform}/weapon-categories"
        data = await self._request(R6API_BASE + endpoint)
        weaponcategories = WeaponCategories(platform=platform, data=data)
        return weaponcategories

    async def get_queue_stats(self, player: str, platform: Platform) -> Queue:
        """
        Get a players queue statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.

        Returns
        -------
        Queue
            Requested player stats
        """
        endpoint = f"/stats/{player}/{platform}/generic"
        data = await self._request(R6API_BASE + endpoint)
        queues = Queue(platform=platform, data=data)
        return queues

    async def get_gamemode_stats(self, player: str, platform: Platform) -> Gamemodes:
        """
        Get gamemode player statistics.

        Paramaters
        ----------
        player: str
            Name of the player to search.
        platform: Platform
            Platform to search.


        Returns
        -------
        Gamemodes
            Requested player stats
        """
        endpoint = f"/stats/{player}/{platform}/generic"
        data = await self._request(R6API_BASE + endpoint)
        gamemodes = Gamemodes(platform=platform, data=data)
        return gamemodes

    async def get_leaderboard(
        self, platform: Platform, region: Regions = Regions.all, page: Optional[int] = 1
    ) -> Leaderboard:
        """
        Get gamemode player statistics.

        Paramaters
        ----------
        platform: Platform
            Platform to search.
        region: Regions
            Region to search.
        page: int
            Page to search, max = 50.


        Returns
        -------
        Leaderboard
            Requested player stats
        """
        if page < 1 or page > 50:
            page = 1
        endpoint = f"/leaderboard/{platform}/{region}?page={page}"
        data = await self._request(R6API_BASE + endpoint)
        gamemodes = Leaderboard(platform=platform, region=region, data=data)
        return gamemodes
