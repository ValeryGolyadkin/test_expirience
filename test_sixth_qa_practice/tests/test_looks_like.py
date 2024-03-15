from test_sixth_qa_practice.pages.look import LikeAButton
import time
import allure


@allure.feature("looks_like_button")
@allure.story("button displayed")
@allure.title("transition")
def test_button_transition(browser):
    like_page = LikeAButton(browser)
    like_page.open()
    assert like_page.button_is_displayed()


@allure.feature("looks_like_button")
@allure.story("button clickable")
@allure.title("looks_click")
def test_button2_click(browser):
    like_page = LikeAButton(browser)
    like_page.open()
    like_page.button_click()
    with allure.step('result'):
        assert 'Submitted' == like_page.result_text()
