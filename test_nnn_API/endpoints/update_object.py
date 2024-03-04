import requests
from test_nnn_API.endpoints.base_andpoint import Endpoint


class UpdateObject(Endpoint):

    def update_by_id(self, obj_id, play_load):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}',
                                     json=play_load).json()
        self.response_json = self.response.json()

    def check_id(self, object_id):
        assert self.response_json['id'] == object_id

    def check_name(self, name):
        assert self.response_json['name'] == name
