Feature: Services

  @wip @empty_cart
  Scenario: Complete Start-to-Finish Package. Add service to cart
    Given I am on Services page
    When I choose Complete Start-to-Finish Package item
    And I add One-School Package to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same

  Scenario: A la Carte Hourly Services. Add service to cart
    Given I am on Services page
    When I choose A la Carte Hourly Services item
    And I choose duration with Purchase 5 hours
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same

  Scenario: Pre-Application Strategy. Add service to cart
    Given I am on Services page
    When I choose Pre-Application Strategy item
    And I choose duration with 4 hours
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same

  Scenario: MBA Application Boot Camp. Add service to cart
    Given I am on Services page
    When I choose MBA Application Boot Camp item
    And I choose class date with Online A
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same
    And the dates and times are the same

  Scenario: Mock Interview Sessions. Add service to cart
    Given I am on Services page
    When I choose Mock Interview Sessions item
    And I choose type of interview with First interview session (Phone or Skype)
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same

  @wip @no_add_to_cart_btn
  Scenario: Ding Review/Re-applicant Strategy. Add service to cart
    Given I am on Services page
    When I choose Ding Review Re-applicant Strategy item
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same

  Scenario: Wharton Team-Based Discussion Simulation. Add service to cart
    Given I am on Services page
    When I choose Wharton Team-Based Discussion Simulation item
    And I want to see that service is Sold out
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has not been added to the cart

  Scenario: HBS Mock Interview and Post-Interview Reflection Support. Add service to cart
    Given I am on Services page
    When I choose HBS Mock Interview and Post-Interview Reflection Support item
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same

  Scenario: Expedited Services. Add service to cart
    Given I am on Services page
    When I choose Expedited Services item
    And I choose select with 3 Expedited Essays
    And I adding this service to cart
    And I view my cart
    Then I want to see that the service has been added to the cart
    And prices are the same
