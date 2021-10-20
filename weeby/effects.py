from . import config
from .util import make_request, image_request

class Image:
    def __init__(self, token) -> None:
        self.token = token

    def general(self, image_url: str, type: str):
        url = config.api_url + f"effects/{type}?image={image_url}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def intensity(self, image_url: str, type: str, intensity: int):
        url = config.api_url + f"effects/{type}?image={image_url}&intensity={str(intensity)}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def level(self, image_url: str, type: str, level: int):
        url = config.api_url + f"effects/{type}?image={image_url}&level={str(level)}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def resize(self, image_url: str, width: int, height: int):
        url = config.api_url + f"effects/resize?image={image_url}&width={str(width)}&height={str(height)}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))