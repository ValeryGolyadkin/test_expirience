import pytest
from test_nnn_api.endpoints.create_Object import CreateObject
from test_nnn_api.endpoints.delete_object import DeleteObject


@pytest.fixture()
def obj_id():
    create_obj = CreateObject()
    play_load = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1344.99,
            "CPU model": "Intel Core i9"
        }
    }
    create_obj.new_object(play_load)
    yield create_obj.response_json["id"]
    delete_obj = DeleteObject()
    delete_obj.delete_object(create_obj.response_json["id"])
