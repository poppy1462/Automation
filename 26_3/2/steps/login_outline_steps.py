from behave import given, when, then

from BrainBucketTesting.pages.login_page import LoginPage


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when('user types "{value}" in "{field}"')
def type_value_in_field(context, value, field):
    login_page = context.login_page

    if value == "None":
        return

    if field == "email":
        login_page.email_input(value)
    elif field == "password":
        login_page.password_input(value)


@when("user clicks Login button")
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_btn()


@then('Warning is shown No match for E-Mail Address and/or Password')
def verify_error_login_form(context):
    login_page = context.login_page
    assert login_page.get_login_error() == "Warning: No match for E-Mail Address and/or Password."


