import requests
from .base_endpoint import Endpoint
import allure


class GetObject(Endpoint):

    def get_object(self, id):
        with allure.step("get response"):
            self.response = requests.get(f'https://api.restful-api.dev/objects/{id}')
            self.response_json = self.response.json()

    def check_id(self, object_id):
        with allure.step("search id"):
            assert self.response_json['id'] == object_id

