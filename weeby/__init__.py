from .json_response import JSON

class Weeby:
    def __init__(self, token: str) -> None:
        self.token = token

    def get_json_response(self):
        return JSON(self.token)