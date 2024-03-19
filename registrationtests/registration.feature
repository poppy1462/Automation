@wip
Feature: Registration functionality

  @positive
  Scenario: User fills out all the fields
    When User fills out all the fields
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

  @negative @skip
  Scenario: User has an existing account
    When Existing user fills out all the fields
    And User chooses United States from the Country dropdown and Illinois from the Region/State dropdown
    And User clicks the checkmark
    And User clicks the Continue button
    Then Existing account alert is shown

    """
    When you select scenarios by one tag:
    behave **/registration.feature --tags=@wip
    When you select scenarios that have one or another tag:
    behave **/registration.feature --tags=@skip,@positive
    When you select scenarios that have 2 tags:
    behave **/registration.feature --tags=@negative --tags=@skip
    When you disable scenarios that have a specific tag:
    behave **/registration.feature --tags=~@negative
    """