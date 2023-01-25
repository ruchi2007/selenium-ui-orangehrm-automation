Feature: orangehrm loginPage
  Background: common steps
    Given i navigate to login page
    When i enter username
    And i enter password
    And i click submit button

  Scenario: user should login successfully with valid parameters
    Then i should login to the dashboard page

  Scenario: logo should be displayed
    Then i should see logo

  Scenario: logout button is displayed
    When i click on profile picture
    Then i should see logout