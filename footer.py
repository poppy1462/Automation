from BrainBucketTesting.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Footer:
    def __init__(self, browser):
        self.about_us_btn = Element(browser, By.XPATH, "//a[contains(.,'About Us')]")
        self.delivery_info_btn = Element(browser, By.XPATH, "//a[contains(.,'Delivery Information')]")
        self.privacy_policy_btn = Element(browser, By.XPATH, "//a[contains(.,'Privacy Policy')]")
        self.terms_btn = Element(browser, By.XPATH, "//a[contains(.,'Terms & Conditions')]")

    def click_about_us(self):
        self.about_us_btn.click()

    def click_delivery_info(self):
        self.delivery_info_btn.click()

    def click_privacy_policy(self):
        self.privacy_policy_btn.click()

    def click_terms(self):
        self.terms_btn.click()