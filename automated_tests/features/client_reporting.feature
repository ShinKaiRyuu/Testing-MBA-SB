Feature: Client Reporting

  Scenario: Filter on Purchase Type
    Given I am logged in as administrator
    And I am on Client Reporting page
    When I choose option Hourly of select Purchase Type
    And I click Search for Client Information
    Then I want to see filtered data

  Scenario: Pagination
    Given I am logged in as administrator
    And I am on Client Reporting page
    And data paginated
    When I click to Next
    Then I want to see new values
    When I click to Previous
    Then I want to see previous values

  Scenario: View client information
    Given I am logged in as administrator
    And I am on Client Reporting page
    When I click on client row
    Then I want to see client information
