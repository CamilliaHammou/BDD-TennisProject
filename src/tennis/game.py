from typing import Optional
from .score import TennisScore, GameState

class TennisGame:
    """on va gérér le score du jeu ."""
        
    def __init__(self, player1_name: str = "Player 1", player2_name: str = "Player 2"):
        """on init une nouvelle parti"""
        self.player1_name = player1_name
        self.player2_name = player2_name
        self._player1_points = 0
        self._player2_points = 0
        self._winner: Optional[str] = None

    def score_point(self, player: str) -> None:
        """on met les points au bon joueur"""
        if self._winner:
            raise ValueError("Game is already finished")
            
        if player == self.player1_name:
            self._player1_points += 1
        elif player == self.player2_name:
            self._player2_points += 1
        else:
            raise ValueError(f"Unknown player: {player}")
            
        self._check_game_end()

    def _check_game_end(self) -> None:
        """on regard si le jeu est fini, si oui on affiche le score"""
        if self._player1_points >= 4 or self._player2_points >= 4:
            point_diff = abs(self._player1_points - self._player2_points)
                    
            if point_diff >= 2:
                if self._player1_points > self._player2_points:
                    self._winner = self.player1_name
                else:
                    self._winner = self.player2_name

    def get_score(self) -> TennisScore:
        """on get le score actuel"""
        state = self._determine_game_state()
            
        return TennisScore(
            player1_points=self._player1_points,
            player2_points=self._player2_points,
            state=state,
            winner=self._winner,
            player1_name=self.player1_name,
            player2_name=self.player2_name
        )

    def _determine_game_state(self) -> GameState:
        """on regarde l'état actuel du jeu"""
        if self._winner:
            return GameState.GAME_WON
            
        if self._player1_points >= 3 and self._player2_points >= 3:
            if self._player1_points == self._player2_points:
                return GameState.DEUCE
            else:
                return GameState.ADVANTAGE
            
        return GameState.REGULAR

    @property
    def is_finished(self) -> bool:
        return self._winner is not None

    @property
    def winner(self) -> Optional[str]:
        return self._winner