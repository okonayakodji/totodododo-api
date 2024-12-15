"""
Module for deep application customization, as well as automatic creation of settings
"""

from os import getenv

PREFIX = "TOTODODODO_"
DB_HOST = getenv(f"{PREFIX}DB_HOST", "")
DB_PORT = getenv(f"{PREFIX}DB_PORT", "")
DB_NAME = getenv(f"{PREFIX}DB_NAME", "")
DB_USER = getenv(f"{PREFIX}DB_USER", "")
DB_PASSWORD = getenv(f"{PREFIX}DB_PASSWORD", "")

__all__ = ["DB_HOST"]
