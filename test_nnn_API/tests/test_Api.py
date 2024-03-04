import requests
import pytest
from test_nnn_API.endpoints.create_Object import CreateObject
from test_nnn_API.endpoints.get_object import GetObject
from test_nnn_API.endpoints.update_object import UpdateObject
from test_nnn_API.endpoints.delete_object import DeleteObject




def test_create_object():
    new_object_endpoint = CreateObject()
    play_load = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1344.99,
            "CPU model": "Intel Core i9"
        }
    }
    new_object_endpoint.new_object(play_load=play_load)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(play_load['name'])


def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_object(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_id(obj_id)


def test_put_object(obj_id):
    play_load = {
        "name": "Apple MacBook Pro 26",
        "data": {
            "year": 2029,
            "price": 11344.99,
            "CPU model": "Intel Core i19"
        }
    }
    update_obj_endpoint = UpdateObject()
    update_obj_endpoint.update_by_id(obj_id, play_load)
    update_obj_endpoint.check_response_is_200()
    update_obj_endpoint.check_name(play_load)


def test_del_object(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_object(obj_id)
    delete_obj_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_object(obj_id)
    get_obj_endpoint.check_response_is_404()
