Feature: Log in. Scoreboard

  Scenario: Successful login as administrator
    Given I am on Scoreboard Main page
    When I click Login button on page
    And I login with username 'Agrossman' and password '111111'
    Then I want to see Billing Reporting page

  Scenario: Successful login as consultant
    Given I am on Scoreboard Main page
    When I click Login button on page
    And I login with username 'Jkedrowski' and password '111111'
    Then I want to see Consultant Dashboard page
    When I click Log out button
    Then I want to see that I am logged out

  Scenario: Unsuccessful login
    Given I am on Scoreboard Main page
    When I click Login button on page
    And I login with username '1111111' and password 'Agrossman'
    Then I want to see error message "Sorry, either Username or Password is incorrect. Please try again."
