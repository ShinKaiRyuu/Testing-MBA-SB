Feature: Billing Reporting

  Scenario: Filter on Purchase Type.
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-01-2015 in Start date field
    And I choose option Hourly of select Purchase Type
    And I click Search for Billing Data button
    Then I want to see filtered data at Billing Report table

  Scenario: Filter on Free Consultation Form Source.
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-01-2015 in Start date field
    And I choose option Google of select Free Consultation Form Source
    And I click Search for Billing Data button
    Then I want to see filtered data at Billing Report table

  Scenario: Filter on Consultant.
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-01-2015 in Start date field
    And I choose option Eric Hollowaty of select Consultant
    And I click Search for Billing Data button
    Then I want to see filtered data at Billing Report table

  Scenario: Filter on Free Consultation Consultant.
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-01-2015 in Start date field
    And I choose option Jessica Shklar of select Free Consultation Consultant
    And I click Search for Billing Data button
    Then I want to see filtered data at Billing Report table

  Scenario: Filter on Start and End date.
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-02-2015 in Start date field
    And I choose 06-02-2015 in End date field
    And I click Search for Billing Data button
    Then I want to see filtered data at Billing Report table

  Scenario: View record on Billing Report table
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I select row
    And I click View selected row button on table
    Then I want to see widget with row information

  Scenario: Find records on Billing Report table
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-01-2015 in Start date field
    And I click Search for Billing Data button
    And I click Find records button on table
    Then I want to see Search record widget
    When I fill in needed search parameters
    And I click Find button on widget
    And I closing widget
    Then I want to see relevant data at Billing Report table

  Scenario: Inactive consultants
    Given I am logged in as administrator
    And I am on Billing Reporting page
    When I choose 06-01-2015 in Start date field
    And I click Search for Billing Data button
    And I click Show inactive consultants button on table
    Then I want to see data with inactive consultants
    When I click Hide inactive consultants button on table
    Then I want to see data without inactive consultants
