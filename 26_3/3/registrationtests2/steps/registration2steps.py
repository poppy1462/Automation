from behave import given, when, then


@when("user fills out all fields")
def enter_all_fields(context):
    context.execute_steps(
        """
        When user enters first name
        And user enters last name
        And user enters email
        And user enters telephone
        And user enters address
        And user enters city
        And user enters password
        And user confirms password
        """
    )


@when("user enters first name")
def enter_first_name(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_first_name(configs.get_user1_first_name())


@when("user enters last name")
def enter_last_name(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_last_name(configs.get_user1_last_name())


@when("user enters email")
def enter_email(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_email(configs.get_user1_email())


@when("user enters telephone")
def enter_telephone(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_telephone(configs.get_user1_telephone())


@when("user enters address")
def enter_address(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_first_line_address(configs.get_user1_address())


@when("user enters city")
def enter_city(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_city(configs.get_user1_city())


@when("user enters password")
def enter_password(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.enter_password(configs.get_user1_password())


@when("user confirms password")
def enter_password(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.confirm_password(configs.get_user1_password())


@when("User fills out all the fields except the Address section")
def enter_all_fields_skip_address(context):
    context.execute_steps(
        """
        When user enters first name
        And user enters last name
        And user enters email
        And user enters telephone
        And user enters city
        And user enters password
        And user confirms password
        """
    )


@when("User chooses United States from the Country dropdown and Illinois from the Region/State dropdown")
def choose_country_and_state(context):
    context.execute_steps(
        """
        When User chooses United States from the Country dropdown
        And User chooses Illinois from the Region/State dropdown
        """
    )


@when("User chooses United States from the Country dropdown")
def choose_country(context):
    registration_page = context.registration_page
    configs = context.configs
    registration_page.select_country(configs.get_user1_country())


@when("User chooses Illinois from the Region/State dropdown")
def choose_state(context):
    registration_page = context.registration_page
    configs = context.configs
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
