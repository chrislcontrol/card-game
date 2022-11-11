import uuid
from typing import List

from src.objects.card import Card


class Player:
    def __init__(self, name: str, is_bot: bool = False):
        self.id = str(uuid.uuid4())
        self.name = name
        self.hand: List[Card] = []
        self.is_bot = is_bot

    def add_cart_to_hand(self, card: Card):
        self.hand.append(card)

    def __str__(self):
        return f"Player[id={self.id}, name={self.name}]"
