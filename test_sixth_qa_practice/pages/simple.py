from selenium.webdriver.common.by import By
from test_sixth_qa_practice.pages.base import BasePage


button_selector = (By.ID, "submit-id-submit")
result_selector = (By.ID, "result-text")


class SimpleButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def button_click(self):
        return self.button().click()

    def result(self):
        return self.find(result_selector)

    def result_text(self):
        return self.result().text

