Feature: Consultant Summary Report

  Scenario: View data as for date
    Given I am logged in as administrator
    And I am on Consultant Summary Report page
    When I choose first day of current month in Date field
    Then I want to see information for that fiscal year up to that Date

  Scenario: Filter Revenue Earned Report by Client
    Given I am logged in as administrator
    And I am on Consultant Summary Report page
    When I click on current month link
    Then I want to see all clients for current month
    When click on client
    Then I want to see all records only for that client
