import pytest


def test_one_is_one(seporate, all_tests):
    print("well done")
    assert 1 == 1


@pytest.mark.skip("2!=32")
def test_two_is_two(seporate):
    assert 2 == 32


@pytest.mark.smoke
def test_three_is_three(seporate):
    assert 3 == 3
    print('joke')

# pytest -v -тест с доп. инфой

# pytest -s - тест с выводом внутреннего текста print
