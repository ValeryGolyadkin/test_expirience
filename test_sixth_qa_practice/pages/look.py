import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_sixth_qa_practice.pages.base import BasePage
button_selector = (By.XPATH, '//*[@class="a-button"]')
result_selector = (By.ID, "result")


class LikeAButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('open_page_s'):
            self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    def button(self):
        with allure.step('button selected'):
            return self.find(button_selector)

    def button_is_displayed(self):
        with allure.step('button displayed'):
            return self.button().is_displayed()

    def button_click(self):
        with allure.step('click'):
            return self.button().send_keys(Keys.RETURN)

    def result(self):
        return self.find(result_selector)

    def result_text(self):
        with allure.step('get result text'):
            return self.result().text
