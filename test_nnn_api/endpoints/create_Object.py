import requests
from .base_endpoint import Endpoint
import allure


class CreateObject(Endpoint):

    def new_object(self, play_load):
        with allure.step("posting response"):
            self.response = requests.post('https://api.restful-api.dev/objects', json=play_load)
            self.response_json = self.response.json()

    def check_name(self, name):
        with allure.step("check name of post"):
            assert self.response_json['name'] == name
