from typing import Dict

import aiohttp

__all__ = (
    "R6StatsApiException",
    "Unauthorized",
    "InternalError",
    "PlayerNotFound",
    "HTTPException",
)


class R6StatsApiException(Exception):
    """Base exception class for R6Stats API."""


class Unauthorized(R6StatsApiException):
    """Exception that's thrown when status code 401 occurs.

    Invalid token."""


class InternalError(R6StatsApiException):
    """Exception that's thrown when the service has an Internal Error caused by HTTP Codes 501 or 503."""


class PlayerNotFound(R6StatsApiException):
    """Exception that's thrown when a player is not found or there is no records availabe. Status Code 404."""


class HTTPException(R6StatsApiException):
    """Exception that's thrown when an HTTP request fails.
    Attributes
    ----------
    response: aiohttp.ClientResponse
        The response of the failed HTTP request.
    status: int
        The status code of the HTTP request.
    message: str
        Details about error.
    """

    def __init__(self, response: aiohttp.ClientResponse, data: Dict) -> None:
        self.response = response
        self.status = response.status
        self.message = data.get("error")
        super().__init__(f"{self.response.reason} (status code: {self.status}): {self.message}")
