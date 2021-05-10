from locator import *
from element import BasePageElement


class LoginUser(BasePageElement):
    locator = "/html/body/div[1]/div/div/form/div[1]/input"


class LoginPass(BasePageElement):
    locator = "/html/body/div/div/div/form/div[2]/input"


class SignupUser(BasePageElement):
    locator = "/html/body/div[1]/div/div/form/div[1]/input"


class SignupMail(BasePageElement):
    locator = "/html/body/div/div/div/form/div[2]/input"


class SignupPass(BasePageElement):
    locator = "/html/body/div/div/div/form/div[3]/input"


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
    user_name = LoginUser()
    user_pass = LoginPass()


class SignupPage(BasePage):
    new_user = SignupUser()
    new_mail = SignupMail()
    new_pass = SignupPass()
