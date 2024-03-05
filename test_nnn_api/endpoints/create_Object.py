import requests
from .base_endpoint import Endpoint


class CreateObject(Endpoint):

    def new_object(self, play_load):
        self.response = requests.post('https://api.restful-api.dev/objects', json=play_load)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name
