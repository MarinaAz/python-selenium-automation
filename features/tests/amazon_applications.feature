# Created by marinaazizbajeva at 25/03/21
Feature: Test for window handling
  # Enter feature description here

  Scenario: Scenario: User can open and close Amazon Applications
 Given Open Amazon T&C page
 When Store original windows
 Then Click on Amazon applications link
 And Switch to the newly opened window
 Then Amazon app page is opened
 And User can close new window and switch back to original

