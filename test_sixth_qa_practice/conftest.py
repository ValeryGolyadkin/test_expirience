import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import allure


@allure.feature('browser_run')
@pytest.fixture()
def browser():
    options = Options()
    with allure.step('headless'):
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
        return browser
