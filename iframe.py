from BrainBucketTesting.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Iframe:
    def __init__(self, browser):
        self.__driver = browser.get_driver()
        self.iframe = Element(browser, By.TAG_NAME, 'iframe')
        self.logo = Element(browser, By.ID, 'intro_logo')

    def switch_to_iframe(self):
        return self.__driver.switch_to.frame(self.iframe.get_element())

    def test_iframe(self):
        iframe = self.switch_to_iframe()
        self.logo.wait_until_visible()
        return self.__driver.switch_to_default_content()
