Feature: Test the login features

@skip_prod
  Scenario: Sing In with a valid account
    Given I am on the Home page
    When I login with the following information
      | email                 | password    | username     |
      | test_account@test.com | Password123 | test account |
    Then The login is done


  Scenario: Create an account
    Given I am on the Home page
    When Create an account with default data
    Then The account creation finish successfully