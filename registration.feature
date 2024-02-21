Feature: Registration functionality
  Background:
    Given Given User launch registration page
  Scenario: User fills out all the fields
    Given User is not logged in
    And User doesn't have an existing account
    When User enters First Name: Will
    * User enters Last Name: Smith
    * User enters E-Mail: will.smith@gmail.com
    * User enters Telephone: 111-222-3344
    * User enters Address 1: 453 White St
    * User enters City: Chicago
    * User chooses Country from the dropdown: United States
    * User chooses Region/State from the dropdown: Illinois
    * User enters Password: Qwerty
    * User enters the same password in Password Canfirm: Qwerty
    And User clicks the check button
    And User clicks the Continue button
    Then User should see a message "New account has been created"
    And Account page is launched


  Scenario: User fills out all the fields except the Address section
    Given User is not logged in
    And User doesn't have an existing account
    When User enters First Name: Jon
    * User enters Last Name: Snow
    * User enters E-Mail: jon.snow@gmail.com
    * User enters Telephone: 111-222-3367
    * User enters Address 1: 498 White St
    * User enters City: Chicago
    * User chooses Country from the dropdown: United States
    * User chooses Region/State from the dropdown: Illinois
    * User enters Password: Qwerty
    * User enters the same password in Password Canfirm: Qwerty
    And User clicks the check button
    And User clicks the Continue button
    Then Warning will be shown "Address 1 must be between 3 and 128 characters!"


  Scenario: User has an existing account
    Given User is not logged in
    And User has an existing account registered under jon.snow@gmail.com
    When User enters First Name: Jon
    * User enters Last Name: Snow
    * User enters E-Mail: jon.snow@gmail.com
    * User enters Telephone: 111-222-3367
    * User enters Address 1: 498 White St
    * User enters City: Chicago
    * User chooses Country from the dropdown: United States
    * User chooses Region/State from the dropdown: Illinois
    * User enters Password: Qwerty
    * User enters the same password in Password Canfirm: Qwerty
    And User clicks the check button
    And User clicks the Continue button
    Then User should see a message "This account already exists"