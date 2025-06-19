import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from tennis.game import TennisGame

scenarios('../features/tennis.feature')

@pytest.fixture
def tennis_game():
    return TennisGame()

@given('a new tennis game')
def new_tennis_game(tennis_game):
    return tennis_game

@given('both players have scored 3 points')
def both_players_scored_three_points(tennis_game):
    for _ in range(3):
        tennis_game.score_point("Player 1")
        tennis_game.score_point("Player 2")

@given('Player 1 has advantage')
def player_1_has_advantage(tennis_game):
    tennis_game.score_point("Player 1")

@given(parsers.parse('Player 1 has scored {points:d} points'))
def player_1_scored_points(tennis_game, points):
    for _ in range(points):
        tennis_game.score_point("Player 1")

@given(parsers.parse('Player 2 has scored {points:d} points'))
def player_2_scored_points(tennis_game, points):
    for _ in range(points):
        tennis_game.score_point("Player 2")

@when('Player 1 scores a point')
def player_1_scores_point(tennis_game):
    tennis_game.score_point("Player 1")

@when('Player 2 scores a point')
def player_2_scores_point(tennis_game):
    tennis_game.score_point("Player 2")

@when('Player 1 scores 4 points')
def player_1_scores_four_points(tennis_game):
    for _ in range(4):
        tennis_game.score_point("Player 1")

@then(parsers.parse('the score should be "{expected_score}"'))
def check_score(tennis_game, expected_score):
    actual_score = tennis_game.get_score().display_score
    assert actual_score == expected_score, f"Expected '{expected_score}', got '{actual_score}'"

@then('the game should be finished')
def game_should_be_finished(tennis_game):
    assert tennis_game.is_finished, "Game should be finished"