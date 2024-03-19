from behave import given, when, then

from BrainBucketTesting.utils.config_reader import ConfigReader
from BrainBucketTesting.webelements.browser import Browser
from BrainBucketTesting.pages.registration_page import RegistrationPage
from BrainBucketTesting.pages.profile_page import ProfilePage

#URL = "https://cleveronly.com/brainbucket/index.php?route=account/register"
#configs = ConfigReader("/Users/anastasiatskhay/PycharmProjects/PythonIntro/BrainBucketTesting/BDDBehave/registrationtests/steps/config.ini")

# @given("User launches registration page")
# def launch_registration_page(context):
#     configs = context.configs
#     browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
#     context.browser = browser

@when("User fills out all the fields")
def fill_out_form(context):
    registration_page = RegistrationPage(context.browser)
    configs = context.configs
    registration_page.enter_first_name(configs.get_user1_first_name())
    registration_page.enter_last_name(configs.get_user1_last_name())
    registration_page.enter_email(configs.get_user1_email())
    registration_page.enter_telephone(configs.get_user1_telephone())
    registration_page.enter_first_line_address(configs.get_user1_address())
    registration_page.enter_city(configs.get_user1_city())
    registration_page.enter_password(configs.get_user1_password())
    registration_page.confirm_password(configs.get_user1_password())
    context.registration_page = RegistrationPage(context.browser)


@when("Existing user fills out all the fields")
def existing_user_fill_out_form(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_first_name(configs.get_user2_first_name())
    registration_page.enter_last_name(configs.get_user2_last_name())
    registration_page.enter_email(configs.get_user2_email())
    registration_page.enter_telephone(configs.get_user2_telephone())
    registration_page.enter_first_line_address(configs.get_user2_address())
    registration_page.enter_city(configs.get_user2_city())
    registration_page.enter_password(configs.get_user2_password())
    registration_page.confirm_password(configs.get_user2_password())


@when("User fills out all the fields except the Address section")
def fill_out_form_except_address(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_first_name(configs.get_user1_first_name())
    registration_page.enter_last_name(configs.get_user1_last_name())
    registration_page.enter_email(configs.get_user1_email())
    registration_page.enter_telephone(configs.get_user1_telephone())
    registration_page.enter_city(configs.get_user1_city())
    registration_page.enter_password(configs.get_user1_password())
    registration_page.confirm_password(configs.get_user1_password())
    context.registration_page = registration_page


@when("User chooses United States from the Country dropdown and Illinois from the Region/State dropdown")
def choose_country_and_state(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.select_country(configs.get_user1_country())
    registration_page.select_state(configs.get_user1_state())


@when("User clicks the checkmark")
def click_checkmark(context):
    registration_page = context.registration_page
    registration_page.agree_to_privacy_policy()


@when("User clicks the Continue button")
def click_continue_button(context):
    registration_page = context.registration_page
    registration_page.submit_form()


@then("Account created title is shown")
def verify_account_created_title(context):
    registration_page = context.registration_page
    assert registration_page.get_form_title() == "Your Account Has Been Created!"


@then("Address alert is shown")
def verify_address_warning(context):
    registration_page = context.registration_page
    assert registration_page.get_address_alert() == "Address 1 must be between 3 and 128 characters!"


@then("Existing account alert is shown")
def verify_account_exists_warning(context):
    registration_page = context.registration_page
    assert registration_page.get_account_exists_alert() == "Warning: E-Mail Address is already registered!"
