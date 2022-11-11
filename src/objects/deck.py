import random
from typing import List

from src.objects.card import Card
from src.objects.suit import Suit

card_string = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}


class Deck:
    def __init__(self):
        self.cards = self.__generate_cards()

    def draw(self, count: int = 1, hiden: int = 0):
        cards = random.choices(self.cards, k=count)

        for card in cards[:hiden]:
            card.hiden = True
        return cards

    def __generate_cards(self) -> List[Card]:
        cards = []
        for string, value in card_string.items():
            for suit in Suit:
                cards.append(Card(value=value, suit=suit, string=string))
        return cards

    def __str__(self):
        return f"Deck[cards={len(self.cards)}]"
