import requests
from .base_endpoint import Endpoint
import allure


class DeleteObject(Endpoint):

    def delete_object(self, obj_id):
        with allure.step("delete response"):
            self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
            self.response_json = self.response.json()
