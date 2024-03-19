from BrainBucketTesting.components.header import Header
from BrainBucketTesting.components.right_menu import RightMenu
from BrainBucketTesting.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from BrainBucketTesting.webelements.dropdown import Dropdown
from BrainBucketTesting.webelements.radiobutton import Radiobutton
from BrainBucketTesting.webelements.radiobutton import Checkbox

class RegistrationPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)

        self.title = Element(browser, By.XPATH, "//*[@id='content']/h1")
        self.first_name_input = Element(browser, By.NAME, "firstname")
        self.last_name_input = Element(browser, By.NAME, "lastname")
        self.email_input = Element(browser, By.NAME, "email")
        self.telephone_input = Element(browser, By.NAME, "telephone")
        self.fax_input = Element(browser, By.NAME, "fax")
        self.company_input = Element(browser, By.NAME, "company")
        self.first_address_input = Element(browser, By.NAME, "address_1")
        self.city_input = Element(browser, By.NAME, "city")
        self.postcode_input = Element(browser, By.NAME, "postcode")
        self.password_input = Element(browser, By.NAME, "password")
        self.confirm_password_input = Element(browser, By.NAME, "confirm")

        self.country_dropdown = Dropdown(browser, By.ID, 'input-country')
        self.region_dropdown = Dropdown(browser, By.NAME, 'zone_id')

        self.subscribe_btn = Radiobutton(browser, By.XPATH, "//input[@name='newsletter' and @value='1']")
        self.unsubscribe_btn = Radiobutton(browser, By.XPATH, "//input[@name='newsletter' and @value='0']")

        self.privacy_policy_checkbox = Checkbox(browser, By.NAME, "agree")

        self.continue_btn = Element(browser, By.XPATH, "//input[@value='Continue']")

        self.address_alert = Element(browser, By.XPATH, "//div[@class='text-danger'][contains(text(), 'Address')]")
        self.account_exists_alert = Element(browser, By.XPATH, "//div[@class='alert alert-danger'][contains(text(), 'registered')]")

    def get_form_title(self):
        return self.title.get_text(wait=True)

    def enter_first_name(self, text):
        self.first_name_input.enter_text(text)

    def enter_last_name(self, text):
        self.last_name_input.enter_text(text)

    def enter_email(self, text):
        self.email_input.enter_text(text)

    def enter_telephone(self, text):
        self.telephone_input.enter_text(text)

    def enter_fax(self, text):
        self.fax_input.enter_text(text)

    def enter_company(self, text):
        self.company_input.enter_text(text)

    def enter_first_line_address(self, text):
        self.first_address_input.enter_text(text)

    def enter_city(self, city):
        self.city_input.enter_text(city)

    def enter_postcode(self, postcode):
        self.postcode_input.enter_text(postcode)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def confirm_password(self, password):
        self.confirm_password_input.enter_text(password)

    def select_country(self, country):
        self.country_dropdown.select_by_text(country)

    def select_state(self, state):
        self.region_dropdown.select_by_text(state)

    def subscribe_to_newsletters(self):
        self.subscribe_btn.select_if_not_selected()

    def unsubscribe_from_newsletters(self):
        self.unsubscribe_btn.select_if_not_selected()

    def agree_to_privacy_policy(self):
        self.privacy_policy_checkbox.select_if_not_selected()

    def submit_form(self):
        self.continue_btn.submit()

    def get_address_alert(self):
        return self.address_alert.get_text()

    def get_account_exists_alert(self):
        return self.account_exists_alert.get_text()
















