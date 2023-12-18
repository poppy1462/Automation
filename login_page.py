from BrainBucketTesting.components.header import Header
from BrainBucketTesting.components.right_menu import RightMenu
from BrainBucketTesting.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        self.email_input_field = Element(browser, By.ID, 'input-email')
        self.password_input_field = Element(browser, By.ID, 'input-password')
        self.login_btn = Element(browser, By.XPATH, "//input[@value='Login']")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

    def email_input(self, email):
        self.email_input_field.enter_text(email)

    def password_input(self, password):
        self.password_input_field.enter_text(password)

    def click_login_btn(self):
        self.login_btn.wait_until_visible()
        self.login_btn.click()
