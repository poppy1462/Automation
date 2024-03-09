from behave import given, when, then

from BrainBucketTesting.utils.config_reader import ConfigReader
from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.pages.registration_page import RegistrationPage
from BrainBucketTesting.pages.profile_page import ProfilePage

URL = "https://cleveronly.com/brainbucket/index.php?route=account/registration"
configs = ConfigReader("/Users/anastasiatskhay/PycharmProjects/PythonIntro/BrainBucketTesting/BDDBehave/registrationtests/steps/config.ini")

@given("user launch registration page")
def launch_registration_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser

@when("User enters First Name, Last Name, E-mail, Telephone, Address, City, Password, Password Confirm")
def fill_out_form(context):
    registration_page = RegistrationPage(context.browser)
    registration_page.enter_first_name(configs.get_user1_first_name())
    registration_page.enter_last_name(configs.get_user1_last_name())
    registration_page.enter_email(configs.get_user1_email())
    registration_page.enter_telephone(configs.get_user1_telephone())
    registration_page.enter_first_line_address(configs.get_user1_address())
    registration_page.enter_city(configs.get_user1_city())
    registration_page.enter_password(configs.get_user1_password())
    registration_page.confirm_password(configs.get_user1_password())

@when("User chooses United States from the Country dropdown")
def choose_country_and_state(context):
    registration_page = RegistrationPage(context.browser)
    registration_page.select_country(configs.get_user1_country())
    registration_page.select_state(configs.get_user1_state())

@when("User clicks the checkmark")
def click_checkmark(context):
    registration_page = RegistrationPage(context.browser)
    registration_page.agree_to_privacy_policy()

@when("User clicks the Continue button")
def click_continue_button(context):
    registration_page = RegistrationPage(context.browser)
    registration_page.submit_form()

@then("user's profile page will be launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"

