"""Exceptions used across Zuni.

Every error here carries a message that is safe to show to the user as-is.
The CLI catches ``ZuniError`` once, prints the message, and exits cleanly
instead of dumping a traceback.
"""


class ZuniError(Exception):
    """Base class for all expected Zuni errors."""


class ConfigError(ZuniError):
    """Missing or invalid configuration (API key, base URL...)."""


class NetworkError(ZuniError):
    """The network request failed (timeout, DNS, connection refused...)."""


class AuthError(ZuniError):
    """The API rejected our credentials (HTTP 401/403)."""


class RateLimitError(ZuniError):
    """The API asked us to slow down (HTTP 429)."""


class APIError(ZuniError):
    """The API answered, but with an error or an unexpected response."""


class SearchError(ZuniError):
    """Web search or page fetching failed."""
