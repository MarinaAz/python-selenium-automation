# Created by marinaazizbajeva at 06/02/21
Feature: Amazon Search Test

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Watch into search field
#    And Click on search icon
#    Then Product results for Watch are shown
#    And First result contains Watch

  Scenario Outline: User can search for a product
    Given Open Amazon page
    When Search for Lamp
    And Click on first product
    And Click on Add to cart button
    Then Verify cart has 1 item

    Examples:
      | search_query | result    |
      | Watches      | "Watches" |
      | Dress        | "Dress"   |

