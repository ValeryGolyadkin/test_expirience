import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        with allure.step('finding_element'):
            return self.browser.find_element(*args)
