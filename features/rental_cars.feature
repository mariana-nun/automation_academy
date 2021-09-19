Feature: Test the rental cars features


Scenario: Search a car
    Given I am on the Home page
    When I search for a car form Mexico to Cancun
    Then I see the first 25 results listed for that cars search


Scenario: Search a car without result
    Given I go to the Home page
    When I search for a car form Charata, Chaco to Resistencia, Chaco
    Then I see the no car results message