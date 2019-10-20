class R6StatsApiException(Exception):
    """Base exception class for R6Stats API."""


class Unauthorized(R6StatsApiException):
    """Exception that's thrown when status code 401 occurs.
    
    Invalid token."""
