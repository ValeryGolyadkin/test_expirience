import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Edge(options=options)
    browser.implicitly_wait(10)
    return browser
