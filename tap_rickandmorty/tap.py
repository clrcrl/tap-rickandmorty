"""RickAndMorty tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_rickandmorty.streams import (
    RickAndMortyStream,
    CharactersStream,
    EpisodesStream,
    LocationsStream,
)

STREAM_TYPES = [
    CharactersStream,
    EpisodesStream,
    LocationsStream,
]


class TapRickAndMorty(Tap):
    """RickAndMorty tap class."""
    name = "tap-rickandmorty"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = {}

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
