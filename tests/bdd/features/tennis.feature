Feature: Tennis Game Scoring
  As a tennis player
  I want to track the score of my game
  So that I know when I've won

  Background:
    Given a new tennis game

  Scenario: New game starts at love all
    Then the score should be "0-0"

  Scenario: Player 1 scores first point
    When Player 1 scores a point
    Then the score should be "15-0"

  Scenario: Player 1 scores two points
    When Player 1 scores a point
    And Player 1 scores a point
    Then the score should be "30-0"

  Scenario: Player 1 scores three points
    When Player 1 scores a point
    And Player 1 scores a point
    And Player 1 scores a point
    Then the score should be "40-0"

  Scenario: Both players score alternately
    When Player 1 scores a point
    And Player 2 scores a point
    And Player 1 scores a point
    And Player 2 scores a point
    Then the score should be "30-30"

  Scenario: Player 2 wins early game
    When Player 2 scores a point
    And Player 2 scores a point
    And Player 2 scores a point
    And Player 2 scores a point
    Then the score should be "Game won by Player 2"
    And the game should be finished

  Scenario: Close game at 40-30
    Given Player 1 has scored 3 points
    And Player 2 has scored 2 points
    When Player 1 scores a point
    Then the score should be "Game won by Player 1"
    And the game should be finished

  Scenario: Deuce situation
    Given both players have scored 3 points
    Then the score should be "Deuce"

  Scenario: Player 1 gets advantage
    Given both players have scored 3 points
    When Player 1 scores a point
    Then the score should be "Advantage Player 1"

  Scenario: Player 2 gets advantage
    Given both players have scored 3 points
    When Player 2 scores a point
    Then the score should be "Advantage Player 2"

  Scenario: Player 1 wins from advantage
    Given both players have scored 3 points
    And Player 1 has advantage
    When Player 1 scores a point
    Then the score should be "Game won by Player 1"
    And the game should be finished

  Scenario: Player 2 wins from advantage
    Given both players have scored 3 points
    And Player 2 has advantage
    When Player 2 scores a point
    Then the score should be "Game won by Player 2"
    And the game should be finished

  Scenario: Back to deuce from advantage
    Given both players have scored 3 points
    And Player 1 has advantage
    When Player 2 scores a point
    Then the score should be "Deuce"

  Scenario: Multiple deuce cycles
    Given both players have scored 3 points
    When Player 1 scores a point
    And Player 2 scores a point
    And Player 1 scores a point
    And Player 2 scores a point
    Then the score should be "Deuce"

  Scenario: Long rally to deuce
    Given Player 1 has scored 2 points
    And Player 2 has scored 3 points
    When Player 1 scores a point
    Then the score should be "Deuce"

  Scenario: Player 1 wins without deuce
    When Player 1 scores 4 points
    Then the score should be "Game won by Player 1"
    And the game should be finished

  Scenario: Score progression 15-15
    When Player 1 scores a point
    And Player 2 scores a point
    Then the score should be "15-15"

  Scenario: Score progression 30-15
    When Player 1 scores a point
    And Player 1 scores a point
    And Player 2 scores a point
    Then the score should be "30-15"

  Scenario: Score progression 15-30
    When Player 2 scores a point
    And Player 2 scores a point
    And Player 1 scores a point
    Then the score should be "15-30"

  Scenario: Score progression 40-30
    Given Player 1 has scored 3 points
    And Player 2 has scored 2 points
    Then the score should be "40-30"

  Scenario: Score progression 30-40
    Given Player 2 has scored 3 points
    And Player 1 has scored 2 points
    Then the score should be "30-40"

  Scenario: Cannot score after game ends
    Given Player 1 has won the game
    When Player 2 attempts to score
    Then an error should be raised

  Scenario: Error handling for unknown player
    When an unknown player attempts to score
    Then an error should be raised

  Scenario: Game state validation
    Given Player 1 has scored 3 points
    And Player 2 has scored 2 points
    Then the game should not be finished
    And the winner should be undefined