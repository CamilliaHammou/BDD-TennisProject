Feature: Tennis Game Scoring
  As a tennis player
  I want to track the score of my game
  So that I know when I've won

  Background:
    Given a new tennis game between Camillia and Denisa

  Scenario: New game starts at love all
    Then the score should be "0-0"

  # Standard progression - grouped for clarity
  Scenario: First point scored
    When Camillia wins her first rally
    Then the score should be "15-0"

  Scenario: Building early momentum  
    When Camillia wins two consecutive rallies
    Then the score should be "30-0"

  Scenario: Reaching game point
    When Camillia wins three consecutive rallies
    Then the score should be "40-0"

  Scenario: Dominating performance
    When Camillia wins four consecutive rallies
    Then the score should be "Game won by Camillia"

  # Competitive exchanges
  Scenario: Trading rallies evenly
    When both players win their opening rally
    Then the score should be "15-15"

  Scenario: Back and forth battle
    When players alternate winning four rallies
    Then the score should be "30-30"

  Scenario: Camillia takes control
    When Camillia leads after three rallies to one
    Then the score should be "30-15"

  Scenario: Denisa fights back
    When Denisa leads after three rallies to one  
    Then the score should be "15-30"

  Scenario: Camillia at game point under pressure
    Given Camillia has scored 3 points
    And Denisa has scored 2 points
    Then the score should be "40-30"

  Scenario: Denisa at game point under pressure
    Given Denisa has scored 3 points
    And Camillia has scored 2 points
    Then the score should be "30-40"

  # Victory scenarios
  Scenario: Denisa claims convincing victory
    When Denisa wins four consecutive rallies
    Then the score should be "Game won by Denisa"

  Scenario: Camillia closes out under pressure
    Given Camillia has scored 3 points
    And Denisa has scored 2 points
    When Camillia wins the decisive rally
    Then the score should be "Game won by Camillia"

  # Deuce situations
  Scenario: Battle reaches deuce
    Given both players have won 3 rallies each
    Then the score should be "Deuce"

  Scenario: Catching up to force deuce
    Given Camillia has scored 2 points
    And Denisa has scored 3 points
    When Camillia wins the equalizing rally
    Then the score should be "Deuce"

  Scenario: Camillia seizes advantage
    Given both players have reached deuce
    When Camillia wins the next rally
    Then the score should be "Advantage Camillia"

  Scenario: Denisa seizes advantage
    Given both players have reached deuce
    When Denisa wins the next rally
    Then the score should be "Advantage Denisa"

  Scenario: Camillia converts advantage to victory
    Given Camillia has advantage after deuce
    When Camillia wins the championship rally
    Then the score should be "Game won by Camillia"

  Scenario: Denisa converts advantage to victory
    Given Denisa has advantage after deuce
    When Denisa wins the championship rally
    Then the score should be "Game won by Denisa"

  Scenario: Advantage neutralized back to deuce
    Given Camillia has advantage after deuce
    When Denisa wins the neutralizing rally
    Then the score should be "Deuce"

  Scenario: Extended deuce battle continues
    Given both players have reached deuce
    When both players win two alternating rallies
    Then the score should return to "Deuce"

  # Game integrity
  Scenario: Game ends - no further scoring allowed
    Given Camillia has won the game
    When Denisa attempts to score
    Then an error should be raised