"""Stream type classes for tap-rickandmorty."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_rickandmorty.client import RickAndMortyStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class CharactersStream(RickAndMortyStream):
    """Define custom stream."""
    name = "characters"
    path = "/character"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "characters.json"
    


class EpisodesStream(RickAndMortyStream):
    """Define custom stream."""
    name = "episodes"
    path = "/episode"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "episodes.json"

class LocationsStream(RickAndMortyStream):
    """Define custom stream."""
    name = "locations"
    path = "/location"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "locations.json"

