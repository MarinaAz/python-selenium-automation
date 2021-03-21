# Created by marinaazizbajeva at 20/03/21
Feature: Amazon Search For Cancelling

  Scenario: User can search for a Cancelling
    Given Open Amazon page
    When Click on Customer Service button
    And Input Cancel Order into Search the help library
    Then Click on search icon
    And Help & Customer Service Page is appears on Amazon
    Then Page URL has Cancel Order in it