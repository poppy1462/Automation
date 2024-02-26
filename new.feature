Feature: Show available products
  Background:
    Given a web browser is at the Brainbucket homepage

  Scenario: Show all available Desktops from the dropdown
    When the user selects See All from the Desktop section in the Navigation Menu
    Then all available Desktops are displayed


  Scenario: Show available Mac Desktops
    When the user selects Mac Desktops from the Navigation Menu
    Then all available Mac Desktops are displayed


  Scenario: Show available PCs
    When the user selects PCs from the Navigation Menu
    Then all available PCs are displayed


  Scenario: Show all available Laptops
    When the user selects See All from the Laptops section in the Navigation Menu
    Then all available Laptops are displayed


  Scenario: Show available Mac Laptops
    When the user selects Mac Laptops from the Navigation Menu
    Then all available Mac Laptops are displayed


  Scenario: Show available Windows Laptops
    When the user selects Windows Laptops from the Navigation Menu
    Then all available Windows Laptops are displayed