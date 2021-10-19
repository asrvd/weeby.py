import requests
import json

def make_request(url: str, headers):
    resp = requests.get(url, headers=headers)
    return(json.loads(resp.content))