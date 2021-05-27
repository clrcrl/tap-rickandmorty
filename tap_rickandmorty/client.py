"""REST client handling, including RickAndMortyStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class RickAndMortyStream(RESTStream):
    """RickAndMorty stream class."""

    url_base = "https://rickandmortyapi.com/api"

    @property
    def http_headers(self) -> dict:
        """No headers needed for this tap, since there's no auth"""
        return {}

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        resp_json = response.json()
        
        # the next token returns a whole URL, need to parse out the page number
        next_page_url = resp_json.get("info").get("next")
        
        if next_page_url:
            # do this the lazy / very bad way for now ;) 
            next_page_token = int(next_page_url.split('page=', 1)[1])
            self.logger.debug(f"Next page token retrieved: {next_page_token}")
            return next_page_token

        return None  # None means we're done. No more pages.

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        resp_json = response.json()
        for row in resp_json.get("results"):
            yield row

