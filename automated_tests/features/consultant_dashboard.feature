Feature: Consultant Dashboard

  Scenario: View data as for date
    Given I am logged in as administrator
    And I am on Consultant Dashboard page
    When I choose first day of current month in Date field
    Then I want to see information for that fiscal year up to that Date

  Scenario: Edit client. Fiscal year
    Given I am logged in as administrator
    And I am on Consultant Dashboard page
    When I select Client Billing table row
    And I click Edit selected row button on table
    And I edit Fiscal year field with 2014
    And I click Save row button on table
    Then I want to see updated row information

  Scenario: Edit client. Contract status
    Given I am logged in as administrator
    And I am on Consultant Dashboard page
    When I select Client Billing table row
    And I click Edit selected row button on table
    And I edit Contract status field with Incomplete
    And I click Save row button on table
    Then I want to see updated row information

  Scenario: Edit client. Consultant
    Given I am logged in as administrator
    And I am on Consultant Dashboard page
    When I select Client Billing table row
    And I click Edit selected row button on table
    And I edit Consultant field with I can't remember
    And I click Save row button on table
    Then I want to see updated row information

  Scenario: Edit client. Free Consultant
    Given I am logged in as administrator
    And I am on Consultant Dashboard page
    When I select Client Billing table row
    And I click Edit selected row button on table
    And I edit Free Consultant field with I can't remember
    And I click Save row button on table
    Then I want to see updated row information

  Scenario: Add invoice
    Given I am logged in as administrator
    And I am on Consultant Dashboard page
    When I see client with Client Status "On"
    And I click "+" on client
    And I click "+" on transaction
    Then I want to be able to add invoice
    When I click Save row button on table
    Then I want to see saved invoice row
