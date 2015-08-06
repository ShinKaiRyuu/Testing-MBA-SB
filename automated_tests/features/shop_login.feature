Feature: Log in. Shopify

  Scenario: Successful login
    Given I am on Login page
    When I login with username 'a@bc.de' and password '111111'
    Then I want to see My Account page
    When I click Log out
    Then I want to see Main page

  Scenario: Unsuccessful login
    Given I am on Login page
    When I login with username 'abcd@ed.ba' and password '111111'
    Then I want to see error message "Invalid login credentials."
