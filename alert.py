from BrainBucketTesting.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Alert:
    def __init__(self, browser):
        self.__driver = browser.get_driver()
        self.alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
        self.confirm_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
        self.prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")
        self.confirm_msg = Element(browser, By.ID, 'msg')
        self.prompt_msg = Element(browser, By.ID, 'demo')

    def switch_to_alert(self):
        return self.__driver.switch_to.alert

    def test_simple_alert(self):
        self.alert_btn.click()
        alert = self.switch_to_alert()
        alert.accept()

    def test_confirmation_alert(self):
        self.confirm_btn.click()
        alert = self.switch_to_alert()
        alert.dismiss()
        assert self.confirm_msg.get_text() == "You pressed CANCEL!"

        self.confirm_btn.click()
        alert = self.switch_to_alert()
        alert.accept()
        assert self.confirm_msg.get_text() == "You pressed OK!"

    def test_prompt_alert(self):
        self.prompt_btn.click()
        alert = self.switch_to_alert()
        name = "Anastasia"
        alert.send_keys(name)
        alert.accept()

        msg = "Hello {}! How are you today?".format(name)
        assert self.prompt_msg.get_text() == msg

