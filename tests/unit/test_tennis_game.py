import pytest
from tennis.game import TennisGame
from tennis.score import GameState

class TestTennisGame:
        
    def test_new_game_starts_at_love_all(self):
        """commence avec 0 0 """
        game = TennisGame("Camillia", "Denisa")
        score = game.get_score()
            
        assert score.player1_points == 0
        assert score.player2_points == 0
        assert score.display_score == "0-0"
        assert score.state == GameState.REGULAR

    def test_player_scores_first_point(self):
        """1 er point"""
        game = TennisGame("Camillia", "Denisa")
        game.score_point("Camillia")
        score = game.get_score()
            
        assert score.display_score == "15-0"

    def test_player_scores_second_point(self):
        """second point"""
        game = TennisGame("Camillia", "Denisa")
        game.score_point("Camillia")
        game.score_point("Camillia")
        score = game.get_score()
            
        assert score.display_score == "30-0"

    def test_player_scores_third_point(self):
        """3 point"""
        game = TennisGame("Camillia", "Denisa")
        game.score_point("Camillia")
        game.score_point("Camillia")
        game.score_point("Camillia")
        score = game.get_score()
            
        assert score.display_score == "40-0"

    def test_both_players_score_three_points_deuce(self):
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(3):
            game.score_point("Camillia")
            game.score_point("Denisa")
            
        score = game.get_score()
        assert score.display_score == "Deuce"
        assert score.state == GameState.DEUCE

    def test_advantage_player_1(self):
        """Camillia est entrain de gagne hehe"""
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(3):
            game.score_point("Camillia")
            game.score_point("Denisa")
            
        # score de cams
        game.score_point("Camillia")
        score = game.get_score()
            
        assert score.display_score == "Advantage Camillia"
        assert score.state == GameState.ADVANTAGE

    def test_advantage_player_2(self):
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(3):
            game.score_point("Camillia")
            game.score_point("Denisa")
            
        game.score_point("Denisa")
        score = game.get_score()
            
        assert score.display_score == "Advantage Denisa"

    def test_win_from_advantage(self):
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(3):
            game.score_point("Camillia")
            game.score_point("Denisa")
            
        game.score_point("Camillia")
        game.score_point("Camillia")
            
        score = game.get_score()
        assert score.display_score == "Game won by Camillia"
        assert game.is_finished
        assert game.winner == "Camillia"

    def test_back_to_deuce_from_advantage(self):
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(3):
            game.score_point("Camillia")
            game.score_point("Denisa")
            
        game.score_point("Camillia")
            
        game.score_point("Denisa")
            
        score = game.get_score()
        assert score.display_score == "Deuce"

    def test_win_without_deuce(self):
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(4):
            game.score_point("Camillia")
            
        score = game.get_score()
        assert score.display_score == "Game won by Camillia"
        assert game.is_finished

    def test_cannot_score_after_game_end(self):
        game = TennisGame("Camillia", "Denisa")
            
        for _ in range(4):
            game.score_point("Camillia")
            
        with pytest.raises(ValueError, match="Game is already finished"):
            game.score_point("Denisa")

    def test_unknown_player_raises_error(self):
        game = TennisGame("Camillia", "Denisa")
            
        with pytest.raises(ValueError, match="Unknown player"):
            game.score_point("Unknown Player")