Feature: Registration

  Scenario: Registration
    Given I am on Registration page
    When I trying to register with
      | f_name | l_name | email          | password |
      | C      | D      | <unique_email> | 111111   |
    Then I want to see My Account page
    And I click Log out
    And I am on Login page
    Then I want be able to login with credentials above
    And I want to see correct customer information


  Scenario: Double registration
    Given I am on Registration page
    When I trying to register with
      | f_name | l_name | email   | password |
      | A      | B      | a@bc.de | 111111   |
    Then I want to see error message "This email address is already associated with an account. If this account is yours, you can reset your password or Login with your credentials"