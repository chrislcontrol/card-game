from abc import ABC, abstractmethod

from src.objects.deck import Deck
from src.objects.option import Option
from src.objects.player import Player
from src.utils.user_interactor import UserInteractor


class Turn(ABC):
    def __init__(self, match, deck: Deck, player: Player):
        self.match = match
        self.deck = deck
        self.player = player

    @abstractmethod
    def start(self):
        raise NotImplementedError()

    def print_cards(self):
        print(f"[{self.player.name}] Suas cartas [{sum(card.value for card in self.player.hand)}/21]:"
              f" obs: [*] = carta escondida")
        for card in self.player.hand:
            print("    ", card)

        print("\n")

    def pass_turn(self):
        print(f"{self.player.name} passou a vez...")
        self.match.next_turn()

    def draw_card(self):
        print(f"{self.player.name} Esta comprando carta...")
        cards = self.deck.draw()

        print(f"{'Cartas compradas' if len(cards) > 1 else 'Carta comprada'}: ", ", ".join(str(card) for card in cards))

        self.player.hand.extend(cards)
        self.match.next_turn()


class PlayerTurn(Turn):
    def start(self):
        self.print_cards()

        while self.match.current_turn == self:
            options = [
                Option(description="Comprar carta", callback=self.draw_card),
                Option(description="Passar vez", callback=self.pass_turn),
                Option(description="Ver sua mao", callback=self.print_cards),
            ]
            UserInteractor(options=options).execute()


class IATurn(Turn):
    def start(self):
        self.pass_turn()
