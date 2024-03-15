import pytest
import allure


@allure.title('one')
@allure.feature("math")
@allure.story("math_1")
def test_one_is_one(seporate, all_tests):
    with allure.step('well done'):
        print("well done")
        assert 1 == 1


@allure.feature("math")
@allure.story("math_2(broke)")
@allure.title('two')
@pytest.mark.skip("2!=32")
def test_two_is_two(seporate):
    with allure.step('broke'):
        assert 2 == 32


@allure.feature("math")
@allure.story("math_3(smoke)")
@allure.title('three')
@pytest.mark.smoke
def test_three_is_three(seporate):
    with allure.step('joke'):
        assert 3 == 3
        print('joke')

# pytest -v -тест с доп. инфой

# pytest -s - тест с выводом внутреннего текста print
