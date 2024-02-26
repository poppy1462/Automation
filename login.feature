Feature: Login functionality
  Background:
    Given a web browser is at the Brainbucket homepage

  Scenario Outline: the user can login using correct email and password
    Given the user is not logged in
    And the user clicks on the Login button from <element>
    When the user enters email and password
    And the user clicks Login button
    Then the user's profile page is launched


  Examples:
    | element        |
    | navigation bar |
    | right menu     |
    | footer         |


  Scenario Outline: User can't login without entering password
    Given the user is not logged in
    And the user clicks on the Login button from <element>
    When the user enters email
    And the user clicks login button
    Then the warning "No match for E-mail Address and/or Password" is shown


  Examples:
    | element        |
    | navigation bar |
    | right menu     |
    | footer         |


  Scenario Outline: User can't login using incorrect email
    Given the user is not logged in
    And the user clicks on the Login button from <element>
    When the user enters incorrect email
    And the user clicks login button
    Then the warning "No match for E-mail Address and/or Password" is shown


  Examples:
    | element        |
    | navigation bar |
    | right menu     |
    | footer         |


  Scenario Outline: User can't login using incorrect password
    Given the user is not logged in
    And the user clicks on the Login button from <element>
    When the user enters correct email
    But the user enters the incorrect password
    And the user clicks login button
    Then the warning "No match for E-mail Address and/or Password" is shown


  Examples:
    | element        |
    | navigation bar |
    | right menu     |
    | footer         |