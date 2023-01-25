Feature: loginPage

  Scenario: user should login successfully with valid parameters
    Given i go to login page
    When i enter username "admin"
    And i enter password "admin123"
    And i click on submit button
    Then i should login successfully to the dashboard page

  Scenario Outline: user should login with Multiple parameters
    Given i go to login page
    When i enter username "<username>"
    And i enter password "<password>"
    And i click on submit button
    Then i should login successfully to the dashboard page
    Examples:
      | username | password |
      | admin    | admin123 |
      | adminxyz | admin123 |
      | admin    | adminxyz |
