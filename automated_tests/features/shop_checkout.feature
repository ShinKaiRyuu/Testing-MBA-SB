Feature: Checkout

  Scenario: Successful checkout
    Given I am logged in with username 'a@bc.de' and password '111111'
    And I have {'type': 'Services', 'item_name': 'HBS Mock Interview and Post-Interview Reflection Support'} in cart
    And I am on Cart page
    And I choose Consultant with 'Adam Grossman' and Free Consultant with 'Dom Poissant'
    And I click Check Out button
    Then I want to see Check Out page
    And product info and price are the same
    When I fill in Billing address form with required data
    And I click Continue to next step button
    Then I want to see Complete My Purchase page
    When I fill in Payment info
    And I click Complete my purchase button
    Then I want to see that purchase completed

  Scenario: Remove products from cart
    Given I have {'type': 'Services', 'item_name': 'HBS Mock Interview and Post-Interview Reflection Support'} in cart
    And I am on Cart page
    When I removing product HBS Mock Interview and Post-Interview Reflection Support
    Then I want to see that removed product not in cart

  Scenario: Checkout. Update button
    Given I have {'type': 'Services', 'item_name': 'HBS Mock Interview and Post-Interview Reflection Support'} in cart
    And I am on Cart page
    And I choose Consultant with 'Eric Hollowaty' and Free Consultant with 'Dom Poissant'
    When I click Update button
    Then I want to see that Consultant and Free Consultant are not changed

  Scenario: Checkout with empty cart
    Given I am on Cart page
    And I want to see that my cart is empty
    And there is no Update, Checkout buttons
