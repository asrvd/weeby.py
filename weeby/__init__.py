from weeby.media import Gif
from weeby.overlays import Overlay
from .json_response import JSON
from .effects import Image
from .overlays import Overlay
from .media import Gif

class Weeby:
    def __init__(self, token: str) -> None:
        self.token = token

    def get_json_response(self) -> JSON:
        return JSON(self.token)

    def apply_effect(self) -> Image:
        return Image(self.token)

    def set_overlay(self) -> Overlay:
        return Overlay(self.token)

    def get_gif(self) -> Gif:
        return Gif(self.token)