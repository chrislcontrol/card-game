from time import sleep
from typing import List

from src.objects.option import Option


class UserInteractor:
    def __init__(self, options: List[Option] = None):
        self.user_input = None
        self._options = options or []
        self._switch = {}

    def execute(self):
        print("Escolha uma opcao: ")
        switch_key = 1
        for option in self._options:
            self._switch[str(switch_key)] = {"callback": option.callback, "description": option.description}
            print(f"{switch_key} - {option.description}")
            switch_key += 1

        self.require_user_input()

        action = self._switch[self.user_input]['callback']
        action()

    def require_user_input(self):
        self.user_input = input("> ")
        description = self._switch[self.user_input]['description']
        print("\n")
        print(f"opcao escolhida: {self.user_input} - {description}")

        sleep(0.333)
