import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from tennis.game import TennisGame

scenarios('../features/tennis.feature')

@pytest.fixture
def tennis_game():
    return TennisGame("Camillia", "Denisa")

# === GIVEN steps ===

@given('a new tennis game between Camillia and Denisa')
def new_tennis_game(tennis_game):
    return tennis_game

@given('Camillia and Denisa both have scored 3 points')
def both_players_scored_three_points(tennis_game):
    for _ in range(3):
        tennis_game.score_point("Camillia")
        tennis_game.score_point("Denisa")

# Nouveau step pour "both players have won 3 rallies each"
@given('both players have won 3 rallies each')
def both_players_won_three_rallies(tennis_game):
    for _ in range(3):
        tennis_game.score_point("Camillia")
        tennis_game.score_point("Denisa")

# Nouveau step pour "both players have reached deuce" 
@given('both players have reached deuce')
def both_players_reached_deuce(tennis_game):
    for _ in range(3):
        tennis_game.score_point("Camillia")
        tennis_game.score_point("Denisa")

@given('Camillia has advantage')
def camillia_has_advantage(tennis_game):
    tennis_game.score_point("Camillia")

# Nouveau step pour "Camillia has advantage after deuce"
@given('Camillia has advantage after deuce')
def camillia_has_advantage_after_deuce(tennis_game):
    # Atteindre deuce d'abord
    for _ in range(3):
        tennis_game.score_point("Camillia")
        tennis_game.score_point("Denisa")
    # Puis advantage
    tennis_game.score_point("Camillia")

# Nouveau step pour "Denisa has advantage after deuce"
@given('Denisa has advantage after deuce')
def denisa_has_advantage_after_deuce(tennis_game):
    # Atteindre deuce d'abord
    for _ in range(3):
        tennis_game.score_point("Camillia")
        tennis_game.score_point("Denisa")
    # Puis advantage
    tennis_game.score_point("Denisa")

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

# === WHEN steps ===

@when('Camillia scores a point')
def camillia_scores_point(tennis_game):
    tennis_game.score_point("Camillia")

@when('Denisa scores a point')
def denisa_scores_point(tennis_game):
    tennis_game.score_point("Denisa")

# Nouveaux steps pour le langage expressif
@when('Camillia wins her first rally')
def camillia_wins_first_rally(tennis_game):
    tennis_game.score_point("Camillia")

@when('Camillia wins two consecutive rallies')
def camillia_wins_two_rallies(tennis_game):
    for _ in range(2):
        tennis_game.score_point("Camillia")

@when('Camillia wins three consecutive rallies')
def camillia_wins_three_rallies(tennis_game):
    for _ in range(3):
        tennis_game.score_point("Camillia")

@when('Camillia wins four consecutive rallies')
def camillia_wins_four_rallies(tennis_game):
    for _ in range(4):
        tennis_game.score_point("Camillia")

@when('Denisa wins four consecutive rallies')
def denisa_wins_four_rallies(tennis_game):
    for _ in range(4):
        tennis_game.score_point("Denisa")

@when('both players win their opening rally')
def both_players_win_opening_rally(tennis_game):
    tennis_game.score_point("Camillia")
    tennis_game.score_point("Denisa")

@when('players alternate winning four rallies')
def players_alternate_four_rallies(tennis_game):
    tennis_game.score_point("Camillia")
    tennis_game.score_point("Denisa")
    tennis_game.score_point("Camillia")
    tennis_game.score_point("Denisa")

@when('Camillia leads after three rallies to one')
def camillia_leads_three_to_one(tennis_game):
    tennis_game.score_point("Camillia")
    tennis_game.score_point("Camillia")
    tennis_game.score_point("Denisa")

@when('Denisa leads after three rallies to one')
def denisa_leads_three_to_one(tennis_game):
    tennis_game.score_point("Denisa")
    tennis_game.score_point("Denisa")
    tennis_game.score_point("Camillia")

@when('Camillia wins the decisive rally')
def camillia_wins_decisive_rally(tennis_game):
    tennis_game.score_point("Camillia")

@when('Camillia wins the equalizing rally')
def camillia_wins_equalizing_rally(tennis_game):
    tennis_game.score_point("Camillia")

@when('Camillia wins the next rally')
def camillia_wins_next_rally(tennis_game):
    tennis_game.score_point("Camillia")

@when('Denisa wins the next rally')
def denisa_wins_next_rally(tennis_game):
    tennis_game.score_point("Denisa")

@when('Camillia wins the championship rally')
def camillia_wins_championship_rally(tennis_game):
    tennis_game.score_point("Camillia")

@when('Denisa wins the championship rally')
def denisa_wins_championship_rally(tennis_game):
    tennis_game.score_point("Denisa")

@when('Denisa wins the neutralizing rally')
def denisa_wins_neutralizing_rally(tennis_game):
    tennis_game.score_point("Denisa")

@when('both players win two alternating rallies')
def both_players_win_two_alternating(tennis_game):
    tennis_game.score_point("Camillia")
    tennis_game.score_point("Denisa")
    tennis_game.score_point("Camillia")
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

# === THEN steps ===

@then(parsers.parse('the score should be "{expected_score}"'))
def check_score(tennis_game, expected_score):
    actual_score = tennis_game.get_score().display_score
    assert actual_score == expected_score, f"Expected '{expected_score}', got '{actual_score}'"

@then(parsers.parse('the score should return to "{expected_score}"'))
def check_score_return(tennis_game, expected_score):
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