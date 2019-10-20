import asyncio
from typing import Optional

import aiohttp

from . import errors
from .enums import Platform
from .player import Player

__all__ = ("Client")
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

    def destroy(self) -> None:
        self._session.detach()

    __del__ = destroy

    async def _get_generic_stats(self, player: str, platform: Platform) -> Player:
        endpoint = f"/stats/{player}/{platform}/generic"
        data = await self._request(R6API_BASE + endpoint)
        player = Player(platform=platform, data=data)
        return player

    async def _get_seasonal_stats(self, player: str, platform: Platform) -> Player:
        endpoint = f"/stats/{player}/{platform}/seasonal"
        data = await self._request(R6API_BASE + endpoint)
        player = Player(platform=platform, data=data)
        return player

    async def _get_operators_stats(self, player: str, platform: Platform) -> Player:
        endpoint = f"/stats/{player}/{platform}/operators"
        data = await self._request(R6API_BASE + endpoint)
        player = Player(platform=platform, data=data)
        return player

    async def _get_weapon_stats(self, player: str, platform: Platform) -> Player:
        endpoint = f"/stats/{player}/{platform}/weapons"
        data = await self._request(R6API_BASE + endpoint)
        player = Player(platform=platform, data=data)
        return player

    async def _get_weaponcategory_stats(self, player: str, platform: Platform) -> Player:
        endpoint = f"/stats/{player}/{platform}/weapon-categories"
        data = await self._request(R6API_BASE + endpoint)
        player = Player(platform=platform, data=data)
        return player
