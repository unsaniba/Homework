# Created by uns at 8/8/23
Feature: Test for Verify these UI elements on Help page

  Scenario: Verify UI elements on Amazon Help Page
    Given Open Amazon help page
    Then Verify Help Page has Card Container
    Then Verify Help Page has Search Box
    Then Verify Help Page has help topics
    Then Verify Help Page has 3 h2 Title


