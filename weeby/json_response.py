from . import config
from .util import make_request

class JSON:
    def __init__(self, token: str) -> None:
        self.token = token

    def random(self, type: str):
        url = config.api_url + "json/" + type.lower()
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(make_request(url, headers)['response'])

    def animal_image(self, type: str):
        url = config.api_url + "json/images/animal/" + type.lower()
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(make_request(url, headers)['url'])

    def meme(self, type: str):
        identifier = {
            "meme" : "meme",
            "memes" : "memes",
            "wholesome" : "wholesomememes",
            "dank" : "dankmemes"
        }
        url = config.api_url + f"json/meme?category={identifier[type.lower()]}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        response = {
            "url" : f"{make_request(url, headers)['url']}",
            "permaLink" : f"{make_request(url, headers)['permaURL']}"
        }
        return(response)

    def word(self, type: str):
        url = config.api_url + f"json/word/{type.lower()}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        if type == "list":
            return(make_request(url, headers))
        else:
            return(make_request(url, headers)['word'])

    def lyrics(self, track: str):
        url = config.api_url + f"json/lyrics?query={track.lower()}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(make_request(url, headers))

    def stats(self):
        url = config.api_url + "json/stats"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(make_request(url, headers))
