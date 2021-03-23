# Created by marinaazizbajeva at 22/03/21
Feature: Test for bestsellers functionality

  Scenario: There are 5 bestsellers links
    Given Open Amazon bestsellers
    Then Verify there are 5 links