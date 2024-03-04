import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Edge()
    browser.implicitly_wait(10)
    return browser
