Feature: Test the search hotel features

@skip_prod
Scenario: Search a hotel
    Given I am on the Home page
    When I search an hotel in Mexico
    Then I see the first 20 results listed for that hotels search

@skip_prod
Scenario: Search a hotel without results
    Given I am on the Home page
    When I search an hotel in Charata, Chaco
    Then I see the no hotel results message

