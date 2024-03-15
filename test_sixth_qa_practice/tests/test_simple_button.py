import allure
from test_sixth_qa_practice.pages.simple import SimpleButton


@allure.feature("simple_button")
@allure.story("button exist")
@allure.title("existed?")
def test_button_exist(browser):
    simple_page = SimpleButton(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()


@allure.feature("simple_button")
@allure.story("button clickable")
@allure.title("looks_click")
def test_button_click(browser):
    simple_page = SimpleButton(browser)
    simple_page.open()
    simple_page.button_click()
    with allure.step('result'):
        assert 'Submitted' == simple_page.result_text()
