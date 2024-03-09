Feature: Registration functionality
  Background:
    Given User launches registration page

  Scenario: User fills out all the fields
    Given User is not logged in
    And User doesn't have an existing account
    When User enters First Name, Last Name, E-mail, Telephone, Address, City, Password, Password Confirm
    And User chooses United States from the Country dropdown and Illinois from the Region/State dropdown
    And User clicks the checkmark
    And User clicks the Continue button
    Then The user's profile page will be launched


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