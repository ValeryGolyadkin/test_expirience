import pytest
# создание функции события с постусловием для теста
@pytest.fixture()  # scope = function -> дефолтное значение
def seporate():
    print('=' * 10)
    yield  # постусловие, предуслоие => return
    print("test finished")


# создание функции события с постусловием
# для всей сэссии от начального до последнего
@pytest.fixture(scope='session')
def all_tests():
    print(1)
    yield
    print('n')