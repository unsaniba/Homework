# Created by uns at 8/7/23
Feature: Test for Home work 4

  Scenario: verify that Bestsellers has amount of links
    Given Open Amazon page
    When Click BESTSELLER
    Then Verify footer has 5 links