Feature: Consultant Administrator Dashboard

  Scenario: View data as for date
    Given I am logged in as administrator
    And I am on Consultant Administrator Dashboard page
    When I choose first day of current month in Date field
    Then I want to see information for that fiscal year up to that Date

  Scenario: Show consultant dashboard
    Given I am logged in as administrator
    And I am on Consultant Administrator Dashboard page
    When I select consultant row
    And I click Show consultant dashboard button on table
    Then I want to see Consultant Dashboard for chosen consultant

  Scenario: Show consultant summary report
    Given I am logged in as administrator
    And I am on Consultant Administrator Dashboard page
    When I select consultant row
    And I click Show consultant summary report button on table
    Then I want to see Consultant Summary Report for chosen consultant

  Scenario: Inactive consultants
    Given I am logged in as administrator
    And I am on Consultant Administrator Dashboard page
    When I click Show inactive consultants button on table
    Then I want to see data with inactive consultants
    When I click Hide inactive consultants button on table
    Then I want to see data without inactive consultants

  Scenario: Only administrators can see Consultant Administrator Dashboard page
    Given I am logged in as consultant
    When I open Consultant Administrator Dashboard page
    Then I want to see message "You are not permissioned to use this feature."
