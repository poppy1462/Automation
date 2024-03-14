from behave import given, when, then

from BrainBucketTesting.utils.config_reader import ConfigReader
from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.pages.login_page import LoginPage
from BrainBucketTesting.pages.profile_page import ProfilePage

URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"
configs = ConfigReader("/Users/anastasiatskhay/PycharmProjects/PythonIntro/BrainBucketTesting/BDDBehave/logintests/steps/config.ini")

@given("user launch login page")
def launch_login_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser

@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning customer"
    context.login_page = login_page

@when("user enters email and password")
def enter_email_and_password(context):
    login_page = context.login_page
    login_page.enter_email(configs.get_user1_email())
    login_page.enter_password(configs.get_user1_password())

@when("user enters email")
def enter_email_only(context):
    login_page = context.login_page
    login_page.enter_email(configs.get_user1_email())

@when("user clicks Login button")
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()

@then("user's profile page will be launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"

@then("Warning will be shown about 'No match for E-Mail Address and/or Password'")
def verify_warning_message(context):
    login_page = context.login_page
    assert login_page.get_error_message() == "Warning: No match for E-Mail Address and/or Password"

