from selenium.webdriver.common.by import By
import time

from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.webelements.UIElement import UIElement as Element
from BrainBucketTesting.webelements.dropdown import Dropdown

from BrainBucketTesting.components.header import Header
from BrainBucketTesting.components.right_menu import RightMenu
from BrainBucketTesting.pages.login_page import LoginPage
from BrainBucketTesting.pages.registration_page import RegistrationPage

URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"


def test_registration_through_dropdown():
    browser = Browser(URL)
    driver = browser.get_driver()

    login_page = LoginPage(browser)
    login_page.email_input(email='test@gmail.com')
    login_page.password_input(password='qwerty123567')
    login_page.click_login_btn()
    time.sleep(5)

    # open registration page from dropdown
    login_page.open_registration_from_account_dropdown()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Mary")
    registration_form.enter_last_name("Jane")
    registration_form.enter_email("hellomary@gmail.com")
    registration_form.enter_telephone("3123404444")
    registration_form.enter_first_line_address("200 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("qwerty123")
    registration_form.confirm_password("qwerty123")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


def test_registration_from_right_menu():
    browser = Browser(URL)
    driver = browser.get_driver()

    login_page = LoginPage(browser)
    login_page.email_input(email='test@gmail.com')
    login_page.password_input(password='qwerty123567')
    login_page.click_login_btn()
    time.sleep(5)

    # open registration page from menu
    login_page.open_registration_from_menu()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Mary")
    registration_form.enter_last_name("Jane")
    registration_form.enter_email("hellomary@gmail.com")
    registration_form.enter_telephone("3123404444")
    registration_form.enter_first_line_address("200 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("qwerty123")
    registration_form.confirm_password("qwerty123")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


if __name__ == "__main__":
    test_registration_through_dropdown()
    test_registration_from_right_menu()
