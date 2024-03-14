@wip
Feature: Login functionality
  Background:
    Given user launch login page

  @positive
  Scenario: a user can login using correct email and password
    Given user is not logged in
    When user enters email and password
    And user clicks Login button
    Then The user's profile page will be launched

  @negative
  Scenario: User can't login without entering password
    Given User is not logged in
    When User enters email
    And User clicks Login button
    Then Warning will be shown about 'No match for E-Mail Address and/or Password'