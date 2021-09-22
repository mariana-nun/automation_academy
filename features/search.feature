Feature: Test the search features

@skip_prod
  Scenario: Search happy path
    Given I am on the Home page
    When I search "dress"
    Then I see the first 7 results listed for that search

@skip_prod
  Scenario: Search that returns no results
    Given I am on the Home page
    When I search "remera"
    Then  I see no results message

