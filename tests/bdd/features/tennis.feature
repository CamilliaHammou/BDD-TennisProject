Feature: Tennis Game Scoring
  As a tennis player
  I want to track the score of my game
  So that I know when I've won

  Background:
    Given a new tennis game between Camillia and Denisa

  Scenario: New game starts at love all
    Then the score should be "0-0"

  Scenario: Camillia scores first point
    When Camillia scores a point
    Then the score should be "15-0"

  Scenario: Camillia takes early lead
    When Camillia scores a point
    And Camillia scores a point
    Then the score should be "30-0"

  Scenario: Camillia reaches game point
    When Camillia scores a point
    And Camillia scores a point
    And Camillia scores a point
    Then the score should be "40-0"

  Scenario: Competitive rally
    When Camillia scores a point
    And Denisa scores a point
    And Camillia scores a point
    And Denisa scores a point
    Then the score should be "30-30"

  Scenario: Denisa wins convincingly
    When Denisa scores a point
    And Denisa scores a point
    And Denisa scores a point
    And Denisa scores a point
    Then the score should be "Game won by Denisa"

  Scenario: Camillia closes out the game
    Given Camillia has scored 3 points
    And Denisa has scored 2 points
    When Camillia scores a point
    Then the score should be "Game won by Camillia"

  Scenario: Deuce situation
    Given Camillia and Denisa both have scored 3 points
    Then the score should be "Deuce"

  Scenario: Camillia gets advantage
    Given Camillia and Denisa both have scored 3 points
    When Camillia scores a point
    Then the score should be "Advantage Camillia"

  Scenario: Denisa gets advantage
    Given Camillia and Denisa both have scored 3 points
    When Denisa scores a point
    Then the score should be "Advantage Denisa"

  Scenario: Camillia wins from advantage
    Given Camillia and Denisa both have scored 3 points
    And Camillia has advantage
    When Camillia scores a point
    Then the score should be "Game won by Camillia"

  Scenario: Denisa wins from advantage
    Given Camillia and Denisa both have scored 3 points
    And Denisa has advantage
    When Denisa scores a point
    Then the score should be "Game won by Denisa"

  Scenario: Back to deuce from advantage
    Given Camillia and Denisa both have scored 3 points
    And Camillia has advantage
    When Denisa scores a point
    Then the score should be "Deuce"

  Scenario: Multiple deuce cycles
    Given Camillia and Denisa both have scored 3 points
    When Camillia scores a point
    And Denisa scores a point
    And Camillia scores a point
    And Denisa scores a point
    Then the score should be "Deuce"

  Scenario: Denisa catches up to deuce
    Given Camillia has scored 2 points
    And Denisa has scored 3 points
    When Camillia scores a point
    Then the score should be "Deuce"

  Scenario: Camillia dominates early
    When Camillia scores 4 points
    Then the score should be "Game won by Camillia"

  Scenario: Even start
    When Camillia scores a point
    And Denisa scores a point
    Then the score should be "15-15"

  Scenario: Camillia leads
    When Camillia scores a point
    And Camillia scores a point
    And Denisa scores a point
    Then the score should be "30-15"

  Scenario: Denisa leads
    When Denisa scores a point
    And Denisa scores a point
    And Camillia scores a point
    Then the score should be "15-30"

  Scenario: Camillia at game point
    Given Camillia has scored 3 points
    And Denisa has scored 2 points
    Then the score should be "40-30"

  Scenario: Denisa at game point
    Given Denisa has scored 3 points
    And Camillia has scored 2 points
    Then the score should be "30-40"

  Scenario: Cannot score after Camillia wins
    Given Camillia has won the game
    When Denisa attempts to score
    Then an error should be raised