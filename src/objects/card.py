from dataclasses import dataclass

from src.objects.suit import Suit


@dataclass
class Card:
    value: int
    string: str
    suit: Suit
    hiden: bool = False

    def __str__(self):
        return f'{self.value} (emblema={self.string}, naipe={self.suit.name}){" [*]" if self.hiden else ""}'

    def __repr__(self):
        return self.__str__()
