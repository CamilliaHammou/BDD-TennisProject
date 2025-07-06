import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from tennis.game import TennisGame

scenarios('../features/tennis.feature')

@pytest.fixture
def tennis_game():
    return TennisGame("Camillia", "Denisa")

@given('a new tennis game between Camillia and Denisa')
def new_tennis_game(tennis_game):
    return tennis_game

@given('Camillia and Denisa both have scored 3 points')
def both_players_scored_three_points(tennis_game):
    for _ in range(3):
        tennis_game.score_point("Camillia")
        tennis_game.score_point("Denisa")

@given('Camillia has advantage')
def camillia_has_advantage(tennis_game):
    tennis_game.score_point("Camillia")

@given('Denisa has advantage')
def denisa_has_advantage(tennis_game):
    tennis_game.score_point("Denisa")

@given(parsers.parse('Camillia has scored {points:d} points'))
def camillia_scored_points(tennis_game, points):
    for _ in range(points):
        tennis_game.score_point("Camillia")

@given(parsers.parse('Denisa has scored {points:d} points'))
def denisa_scored_points(tennis_game, points):
    for _ in range(points):
        tennis_game.score_point("Denisa")

@given('Camillia has won the game')
def camillia_has_won_game(tennis_game):
    for _ in range(4):
        tennis_game.score_point("Camillia")


@when('Camillia scores a point')
def camillia_scores_point(tennis_game):
    tennis_game.score_point("Camillia")

@when('Denisa scores a point')
def denisa_scores_point(tennis_game):
    tennis_game.score_point("Denisa")

@when('Camillia scores 4 points')
def camillia_scores_four_points(tennis_game):
    for _ in range(4):
        tennis_game.score_point("Camillia")

@when('Denisa attempts to score')
def denisa_attempts_to_score(tennis_game):
    with pytest.raises(ValueError):
        tennis_game.score_point("Denisa")

@when('an unknown player attempts to score')
def unknown_player_attempts_to_score(tennis_game):
    with pytest.raises(ValueError):
        tennis_game.score_point("Unknown Player")

@then(parsers.parse('the score should be "{expected_score}"'))
def check_score(tennis_game, expected_score):
    actual_score = tennis_game.get_score().display_score
    assert actual_score == expected_score, f"Expected '{expected_score}', got '{actual_score}'"

@then('the game should be finished')
def game_should_be_finished(tennis_game):
    assert tennis_game.is_finished, "Game should be finished"

@then('the game should not be finished')
def game_should_not_be_finished(tennis_game):
    assert not tennis_game.is_finished, "Game should not be finished"

@then('the winner should be undefined')
def winner_should_be_undefined(tennis_game):
    assert tennis_game.winner is None, "Winner should be undefined"

@then('an error should be raised')
def error_should_be_raised():
    pass