import requests
from test_nnn_api.endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_object(self, id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{id}')
        self.response_json = self.response.json()

    def check_id(self, object_id):
        assert self.response_json['id'] == object_id

