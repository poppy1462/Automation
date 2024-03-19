@wip
Feature: Registration functionality

  @positive
  Scenario: User fills out all the fields
    When user fills out all fields
    And User chooses United States from the Country dropdown and Illinois from the Region/State dropdown
    And User clicks the checkmark
    And User clicks the Continue button
    Then Account created title is shown

  @negative
  Scenario: User fills out all the fields except the Address section
    When User fills out all the fields except the Address section
    And User chooses United States from the Country dropdown and Illinois from the Region/State dropdown
    And User clicks the checkmark
    And User clicks the Continue button
    Then Address alert is shown
