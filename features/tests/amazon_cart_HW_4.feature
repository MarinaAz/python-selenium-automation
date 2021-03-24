# Created by marinaazizbajeva at 06/02/21
Feature: Amazon Search Test

  Scenario : User can search for a product
    Given Open Google page
    When Input Watch into search field
    And Click on search icon
    Then Product results for Watch are shown
    And First result contains Watch


#  Scenario Outline: User can add a product to the cart
#    Given Open Amazon page
#    When Search for Lamp
#    When Click on first product
#    And Click on Add to cart button
#    Then Verify cart has 1 item
#
#  Examples:
#      | search_query | result    |
#      | Watches      | "Watches" |
#      | Dress        | "Dress"   |
#      | Lamp         | "Lamp"    |
#
#  Scenario: User can add a product to the cart
#    Given Open Amazon page
#    When Search for Dress
#    And Click on first product
#    And Select Dress size
#    And Click on Add to cart button
#    Then Verify cart has 1 item

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Dress
    And Click on first product
    And Click on Add to cart button
    Then Verify cart has 1 item