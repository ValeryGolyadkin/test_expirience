from test_sixth_qa_practice.pages.simple import SimpleButton
import time


def test_button_exist(browser):
    simple_page = SimpleButton(browser)
    simple_page.open()
    time.sleep(0.5)
    assert simple_page.button_is_displayed()


def test_button_click(browser):
    simple_page = SimpleButton(browser)
    simple_page.open()
    simple_page.button_click()
    time.sleep(0.5)
    assert 'Submitted' == simple_page.result_text()
