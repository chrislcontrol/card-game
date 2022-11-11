from typing import List

from src.objects.player import Player


class Settings:
    def __init__(self):
        self.players: List[Player] = []

    def add_player(self, player: Player):
        self.players.append(player)

    @property
    def has_players_created(self) -> bool:
        return bool(self.players)
