import requests
from .base_endpoint import Endpoint
import allure


class UpdateObject(Endpoint):

    def update_by_id(self, obj_id, play_load):
        with allure.step("update response"):
            self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}',
                                         json=play_load)
            self.response_json = self.response.json()

    def check_id(self, object_id):
        with allure.step("updated id"):
            assert self.response_json['id'] == object_id

    def check_name(self, name):
        with allure.step("updated name"):
            assert self.response_json['name'] == name
