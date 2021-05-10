from locator import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def title_check(self):
        if "TumorInsight" in self.driver.title:
            status = "PASSED"
        else:
            status = "FAILED"
        print("Test 1: Checking Title of the Web Application --> " + status)
        return "TumorInsight" in self.driver.title

    def go_to_github(self):
        element = self.driver.find_element(*MainPageLocators.GITHUB_SOCIAL)
        element.click()

    def go_to_login(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def go_to_signup(self):
        element = self.driver.find_element(*MainPageLocators.SIGNUP_BUTTON)
        element.click()


class LoginPage(BasePage):
    pass


class SignupPage(BasePage):
    pass
