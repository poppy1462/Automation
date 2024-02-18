from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.UIElement import UIElement as Element
from BrainBucketTesting.webelements.alert import Alert
from BrainBucketTesting.webelements.iframe import Iframe
from selenium.webdriver.common.by import By
import time

URL = "https://cleveronly.com/practice"
browser = Browser(URL)
driver = browser.get_driver()


def test_simple_alert():
    alert = Alert(browser)
    alert.test_simple_alert()
    browser.shutdown()


def test_confirmation_alert():
    alert = Alert(browser)
    alert.test_confirmation_alert()
    browser.shutdown()


def test_prompt_alert():
    alert = Alert(browser)
    alert.test_prompt_alert()
    browser.shutdown()


def test_iframe():
    iframe = Iframe(browser)
    iframe.test_iframe()
    browser.shutdown()



if __name__ == "__main__":
    test_simple_alert()
    test_confirmation_alert()
    test_prompt_alert()
    test_iframe()