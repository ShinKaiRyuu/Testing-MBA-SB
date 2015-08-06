Feature: Core issues

  Scenario: Check transaction
    Given I am new registered customer
    And I have {'type': 'Services', 'item_name': 'HBS Mock Interview and Post-Interview Reflection Support'} in cart
    And I am on Cart page
    And I choose Consultant with 'Adam Grossman' and Free Consultant with 'Dom Poissant'
    And I complete my purchase
    Given I am logged in as administrator
    And I have new transaction
    And I am on Manage Billing page
    Then I want to see new transaction
    And I am on Billing Reporting page
    Then I want to see new transaction
    And I am on Consultant Dashboard page
    Then I want to see new transaction
