import pytest
import allure
from test_nnn_api.endpoints.create_Object import CreateObject
from test_nnn_api.endpoints.get_object import GetObject
from test_nnn_api.endpoints.update_object import UpdateObject
from test_nnn_api.endpoints.delete_object import DeleteObject


@allure.story("CREATE->get->update->delete")
@allure.title("CREATE")
@allure.feature("create")
@pytest.mark.smoke
def test_create_object():
    with allure.step("connect endpoint repo"):
        new_object_endpoint = CreateObject()
    with allure.step("new object"):
        play_load = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1344.99,
                "CPU model": "Intel Core i9"
            }
        }
    with allure.step("post obj"):
        new_object_endpoint.new_object(play_load=play_load)
    with allure.step("check status is 200"):
        new_object_endpoint.check_response_is_200()
    with allure.step("check obj name"):
        new_object_endpoint.check_name(play_load['name'])


@allure.story("create->GET->update->delete")
@allure.title("GET")
@allure.feature("GET")
def test_get_object(obj_id):
    with allure.step("connect endpoint repo"):
        get_obj_endpoint = GetObject()
    with allure.step("get obj by id"):
        get_obj_endpoint.get_object(obj_id)
    with allure.step("check status is 200"):
        get_obj_endpoint.check_response_is_200()
    with allure.step("check obj id"):
        get_obj_endpoint.check_id(obj_id)


@allure.story("create->get->UPDATE->delete")
@allure.title("UPDATE")
@allure.feature("UPDATE")
@pytest.mark.smoke
def test_put_object(obj_id):
    with allure.step("connect endpoint repo"):
        update_obj_endpoint = UpdateObject()
    with allure.step("updated object"):
        play_load = {
            "name": "Apple MacBook Pro 26",
            "data": {
                "year": 2029,
                "price": 11344.99,
                "CPU model": "Intel Core i19"
            }
        }
    update_obj_endpoint.update_by_id(obj_id, play_load)
    with allure.step("check status is 200"):
        update_obj_endpoint.check_response_is_200()
    with allure.step("check updated obj name"):
        update_obj_endpoint.check_name(play_load["name"])


@allure.story("create->get->update->DELETE")
@allure.title("DELETE")
@allure.feature("DELETE")
def test_del_object(obj_id):
    with allure.step("connect endpoint repo"):
        delete_obj_endpoint = DeleteObject()
        get_obj_endpoint = GetObject()
    with allure.step("delete obj"):
        delete_obj_endpoint.delete_object(obj_id)
    with allure.step("check status is 200"):
        delete_obj_endpoint.check_response_is_200()
    with allure.step("get deleted obj id"):
        get_obj_endpoint.get_object(obj_id)
    with allure.step("check status is 404"):
        get_obj_endpoint.check_response_is_404()
