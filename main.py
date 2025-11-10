import random
from color import Color


class Game:
    def __init__(self):
        self.tries = []
        self.word = None
        self.random_word()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def random_word(self):
        with open("words.txt") as file:
            words = file.read().splitlines()
            random_line = random.randint(0, len(words))
            self.word = words[random_line]

    def show_keyboard(self):
        print(f"{'__' * len(self.alphabet) * 2}")
        print(" " + " | ".join(list(self.alphabet)))
        print(f"{'__' * len(self.alphabet) * 2}")


if __name__ == '__main__':
    game = Game()
    game.show_keyboard()
