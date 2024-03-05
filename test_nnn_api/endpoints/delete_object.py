import requests
from .base_endpoint import Endpoint


class DeleteObject(Endpoint):

    def delete_object(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()
