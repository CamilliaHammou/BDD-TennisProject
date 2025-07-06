from enum import Enum
from typing import NamedTuple, Optional

class GameState(Enum):
    """ici on va representer les differentes etape d'un match de tennis"""
    REGULAR = "regular"
    DEUCE = "deuce"
    ADVANTAGE = "advantage"
    GAME_WON = "game_won"

class TennisScore(NamedTuple):
    """ici le score de tenis """
    player1_points: int
    player2_points: int
    state: GameState
    winner: Optional[str] = None
    player1_name: str = "Player 1"
    player2_name: str = "Player 2"
        
    @property
    def display_score(self) -> str:
        """on affiche le score"""
        if self.state == GameState.GAME_WON:
            return f"Game won by {self.winner}"
            
        if self.state == GameState.DEUCE:
            return "Deuce"
            
        if self.state == GameState.ADVANTAGE:
            if self.player1_points > self.player2_points:
                return f"Advantage {self.player1_name}"
            else:
                return f"Advantage {self.player2_name}"
            
        score_map = {0: "0", 1: "15", 2: "30", 3: "40"}
        p1_score = score_map[self.player1_points]
        p2_score = score_map[self.player2_points]
            
        return f"{p1_score}-{p2_score}"