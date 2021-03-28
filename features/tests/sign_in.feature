# Created by marinaazizbajeva at 25/03/21
Feature: Amazon Sign In tests

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page is opens

  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify sign in is clickable
    When Wait for 8 seconds
    Then Verify sign in is clickable
    Then Verify sign in is disappears

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opens
