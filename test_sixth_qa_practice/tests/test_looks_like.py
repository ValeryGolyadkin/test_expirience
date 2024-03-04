from selenium.webdriver.common.by import By
from test_sixth_qa_practice.pages.look import LikeAButton
import time


def test_button_transition(browser):
    like_page = LikeAButton(browser)
    like_page.open()
    time.sleep(0.5)
    assert like_page.button_is_displayed()


def test_button2_click(browser):
    like_page = LikeAButton(browser)
    like_page.open()
    like_page.button_click()
    time.sleep(0.5)
    assert 'Submitted' == like_page.result_text()
