# Created by marinaazizbajeva at 26/03/21
Feature: Test for jeans selection
  # Enter feature description here

  Scenario: User can select jeans color
    Given Open Amazon page of product B07BJKRR25
    When Verify user can click through colors
    Then Click on Add to cart button
    And Verify cart has 1 item
