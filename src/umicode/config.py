"""
Configuration loader for UMICODE.

Loads and validates YAML configuration files.
"""

from pathlib import Path

import yaml

from .exceptions import ConfigurationError


def load_config(path: str | Path) -> dict:
    """
    Load a YAML configuration file.

    Parameters
    ----------
    path
        Path to a YAML configuration file.

    Returns
    -------
    dict
        Parsed configuration dictionary.

    Raises
    ------
    ConfigurationError
        If the configuration cannot be loaded.
    """

    path = Path(path)

    if not path.exists():
        raise ConfigurationError(f"Configuration file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as handle:
            config = yaml.safe_load(handle)

    except yaml.YAMLError as exc:
        raise ConfigurationError(
            f"Invalid YAML in configuration file: {path}"
        ) from exc

    return config