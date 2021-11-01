from . import config
from .util import image_request

class Generator:
    def __init__(self, token: str) -> None:
        self.token = token

    def one_image(self, type: str, url: str):
        url = config.api_url + f"generators/{type}?image={image_url}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def two_image(self, type: str, url1: str, url2: str):
        url = config.api_url + f"generators/{type}?firstimage={url1}&secondimage={url2}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def text(self, type: str, text: str):
        url = config.api_url + f"generators/{type}?text={text}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def two_text(self, type:str, text1: str, text2: str):
        url = config.api_url + f"generators/{type}?textone={text1}&texttwo={text2}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def image_text(self, type: str, url: str, text: str):
        url = config.api_url + f"generators/{type}?image={url}&text={text}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def eject(self, url: str, text: str, outcome: str):
        url = config.api_url + f"generators/eject?image={url}&text={text}&outcome={outcome}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def friendship(self, url1: str, url2: str, text1: str, text2: str):
        url = config.api_url + f"generators/friendship?firstimage={url1}&secondimage={url2}&firsttext={text1}&secondtext={text2}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def demotivational(self, url: str, title: str, text: str):
        url = config.api_url + f"generators/demotivational?image={url}&title={title}&text={text}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def rip(self, url: str, name: str, message: str):
        url = config.api_url + f"generators/rip?avatar={url}&username={name}&message={message}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def tweet(self, url: str, name: str, text: str):
        url = config.api_url + f"generators/tweet?username={name}&tweet={text}&avatar={url}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def tweet_fetch(self, name: str, text: str):
        url = config.api_url + f"generators/tweetfetch?username={name}&tweet={text}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def triggered(self, url: str, tint: bool):
        url = config.api_url + f"generators/triggered?image={url}&tint={tint}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def currency(self, type: str, amount: int):
        url = config.api_url + f"generators/currency?type={type}&amount={str(amount)}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def color(self, hex: str):
        url = config.api_url + f"generators/color?hex={hex}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def spotify(self, url: str, hex: str, text: str):
        url = config.api_url + f"generators/thisisspotify?image={url}&text={text}&color={hex}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

    def spotifynp(self, url: str, title: str, artist: str, album: str):
        url = config.api_url + f"generators/spotifynp?image={url}&title={title}&artist={artist}&album={album}"
        headers= {"Authorization" : f"Bearer {self.token}"}
        return(image_request(url, headers))

