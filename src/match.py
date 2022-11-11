from itertools import cycle

from src.objects.deck import Deck
from src.objects.player import Player
from src.turn import PlayerTurn, IATurn


class Match:
    def __init__(self, player: Player):
        self.player = player
        self.bot = Player(name="Bot", is_bot=True)
        self.deck = Deck()
        self.turns = cycle([PlayerTurn(match=self, deck=self.deck, player=self.player),
                            IATurn(player=self.bot, deck=self.deck, match=self)])
        self.current_turn = None

    def start(self):
        print("Iniciando a partida... \n")
        self.player.hand = self.deck.draw(2, hiden=1)
        self.bot.hand = self.deck.draw(2, hiden=1)

        self.next_turn()

    def next_turn(self):
        self.current_turn = next(self.turns)
        self.current_turn.start()
