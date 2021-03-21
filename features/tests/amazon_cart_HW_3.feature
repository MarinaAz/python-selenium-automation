# Created by marinaazizbajeva at 20/03/21
Feature: Amazon check cart

  Scenario: User can check a cart
    Given Open Amazon page
    When Click on Cart Icon
    And Cart page is appears on Amazon
    Then Page URL has Your Amazon Cart is empty in it