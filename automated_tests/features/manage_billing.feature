@slow
Feature: Manage Billing

  Scenario: Add new row
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I click Add new row button on table
    Then I want to see Add record widget
    When I fill in the form with needed data
    And I click Submit button on widget
    And I closing confirmation widget
    When I reloading page
    Then I want to see added row at Billing Data table

  Scenario: Add new row. Cancel button
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I click Add new row button on table
    Then I want to see Add record widget
    When I fill in the form with needed data
    And I click Cancel button on widget
    Then I want to see no added row at Billing Data table

  Scenario: Edit row
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click Edit selected row button on table
    Then I want to see Edit record widget
    And row information on widget
    When I fill in the form with needed data
    And I click Submit button on widget
    And I closing confirmation widget
    When I click Reload Grid button on table
    Then I want to see edited row at Billing Data table

  Scenario: Edit row. Cancel button
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click Edit selected row button on table
    Then I want to see Edit record widget
    And row information on widget
    When I fill in the form with needed data
    And I click Cancel button on widget
    Then I want to see unedited row at Billing Data table

  Scenario: View record
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click View selected row button on table
    Then I want to see widget with row information

  Scenario: Delete row
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click Delete selected row button on table
    Then I want to see Delete widget
    And I click Delete button on widget
    Then I want to see that row has been deleted

  Scenario: Delete row. Cancel button
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click Delete selected row button on table
    Then I want to see Delete widget
    And I click Cancel button on widget
    Then I want to see that row at Billing Data table

  Scenario: Find records
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I click Find records button on table
    Then I want to see Search records widget
    When I fill in needed search parameters
    And I click Find button on widget
    And I closing widget
    Then I want to see relevant data at Billing Data table

  Scenario: Copy record
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click Copy Record button on table
    Then I want to see Copy record widget
    When I fill in the form with needed data
    And I click Submit button on widget
    And I closing confirmation widget
    When I reloading page
    Then I want to see copied record

  Scenario: Show item changes
    Given I am logged in as administrator
    And I am on Manage Billing page
    When I select row
    And I click Edit selected row button on table
    When I fill in the form with needed data
    And I click Submit button on widget
    And I closing confirmation widget
    And I click Reload Grid button on table
    When I select row
    And I click Show item changes button on table
    Then I want to see Auditing of the user widget
    And fields values before editing on it
