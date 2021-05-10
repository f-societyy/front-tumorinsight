from selenium import webdriver
import unittest
import page
from helper import test_result


class TumorInsightTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

        # TumorInsight is running locally on http://127.0.0.1:5000/
        self.driver.get("http://127.0.0.1:5000/")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.title_check()

    def test_login_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.go_to_login()
        assert "Login" in self.driver.title

    def test_signup_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.go_to_signup()
        assert "Register" in self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
