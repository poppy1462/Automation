from BrainBucketTesting.webelements.UIElement import UIElement as Element
from selenium.webdriver.support.select import Select


class Radiobutton(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select_if_not_selected(self):
        if not self.get_element().is_selected():
            self.click()


class Checkbox(Element):
    def __init__(self,browser, by, locator):
        super().__init__(browser, by, locator)

    def select_if_not_selected(self):
        if not self.get_element().is_selected():
            self.click()


