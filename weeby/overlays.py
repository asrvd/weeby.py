from . import config
from .util import make_request, image_request

class Overlay:
    def __init__(self, token: str) -> None:
        self.token = token

    def overlay(self, type: str, image_url: str):
        url = config.api_url + f"overlays/{type}?image={image_url}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))