from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.UIElement import UIElement as Element

browser = Browser("https://cleveronly.com/brainbucket")
driver = browser.get_driver()

account_btn = Element(browser, By.XPATH, "//a[@title='My Accoun']")
account_btn.get_element()