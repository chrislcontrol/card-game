from match import Match
from src.objects.player import Player
from src.settings import Settings


class Game:
    def __init__(self, game_settings: Settings):
        self.settings = game_settings
        self.match = None

    def start(self):
        print("Bem vindo ao jogo!")

        player = self.select_or_create_player()

        print(f"Ola, {player.name}!")

        print("1 - Iniciar uma partida")
        print("2 - Sair do jogo")
        user_input = input("O que gostaria de fazer? \n > ")

        action = {"1": self.start_match, "2": self.exit_game}[user_input]

        action()

    def select_or_create_player(self) -> Player:
        if self.settings.has_players_created:
            return self.select_player()

        return self.create_player()

    def start_match(self):
        self.match = Match(player=self.settings.players[0])
        self.match.start()

    def select_player(self) -> Player:
        print("Selecione um jogador:")
        for index, player in enumerate(self.settings.players):
            print(f"{index + 1} - {player.name}")

        player_index = input("> ")

        return self.settings.players[int(player_index) - 1]

    def exit_game(self):
        print("Tchau, tchau!")
        exit()

    def create_player(self) -> Player:
        print("Vamos cadastrar um novo jogador.")
        name = input("Qual o seu nome? \n > ")
        player = Player(name=name)
        self.settings.add_player(player)

        return player


if __name__ == "__main__":
    _settings = Settings()
    _game = Game(game_settings=_settings)

    while True:
        _game.start()

        input('Press any key to continue...')
