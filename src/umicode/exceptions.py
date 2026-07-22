"""
Custom exceptions used throughout UMICODE.
"""


class UMICodeError(Exception):
    """Base exception for all UMICODE errors."""


class ConfigurationError(UMICodeError):
    """Raised when a configuration file is invalid."""