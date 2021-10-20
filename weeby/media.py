from . import config
from .util import make_request

class Gif:
    def __init__(self, token: str) -> None:
        self.token = token

    def gif(self, type: str):
        url = config.api_url + f"gif/{type}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(make_request(url, headers)['url'])