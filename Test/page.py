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

