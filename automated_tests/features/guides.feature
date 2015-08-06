Feature: Guides

  Scenario: Insider's Guides. Anderson School of Management Insider's Guide. Add guide to cart
    Given I am on Guides page
    When I choose Insider's Guide guide
    And I view Columbia Business School details
    And I adding this guide to cart
    When I view my cart
    Then I want to see that the guide has been added to the cart
    And prices are the same

  Scenario: Interview Guides. Harvard Business School Interview Guide. Add guide to cart
    Given I am on Guides page
    When I choose Interview Guides guide
    When I view Harvard Business School details
    And I adding this guide to cart
    When I view my cart
    Then I want to see that the guide has been added to the cart
    And prices are the same

  Scenario: Admissions Guides. mbaMission Waitlist Guide. Add guide to cart
    Given I am on Guides page
    When I choose Admissions guide
    When I view mbaMission Waitlist Guide details
    And I adding this guide to cart
    When I view my cart
    Then I want to see that the guide has been added to the cart
    And prices are the same
