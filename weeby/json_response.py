from . import config
from .util import make_request

class JSON:
    def __init__(self, token: str) -> None:
        self.token = token

    def random(self, type: str):
        url = config.api_url + "json/" + type.lower()
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(make_request(url, headers))