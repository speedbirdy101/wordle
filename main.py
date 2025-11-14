import random
from color import Color
import os


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        self.tries = []
        self.word = ""
        self.random_word()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.word_attempts = []
        self.characters = {c: "" for c in self.alphabet}

    def check_word_exists(self, attempt):
        return True  # Just for now

    def random_word(self):
        with open("words.txt") as file:
            words = file.read().splitlines()
            random_line = random.randint(0, len(words))
            self.word = words[random_line]

    def char_checker(self, char):
        char = char.upper()
        return f"{self.characters[char]}{char}{Color.OFF}"

    def show_keyboard(self):
        print(f"{'__' * len(self.alphabet) * 2}")
        print(
            " " + " | ".join(
                map(self.char_checker, self.characters)
            )
        )
        print(f"{'--' * len(self.alphabet) * 2}")

    def incorrect_attempt(self, msg):
        clear()
        self.show_keyboard()
        self.display_attempts()
        print(f"{Color.RED}{msg}, please try again{Color.OFF}")

        return self.take_attempt()

    def take_attempt(self):
        attempt = input("Please enter a word to try: [5 letters only]\n")
        print(f"ATTEMPT: {attempt}")

        # Validify the attempt
        if len(attempt) != 5:
            return self.incorrect_attempt("Not 5 letters")

        if not attempt.isalpha():
            return self.incorrect_attempt("Must only contain letters")

        if not self.check_word_exists(attempt):
            return self.incorrect_attempt("Word does not exist")

        return attempt

    def colour_word(self, word):
        list_word = []
        for index, char in enumerate(word):
            if index == self.word.index(char):
                list_word.append(
                    f"{Color.GREEN}{char}{Color.OFF}"
                )

    def display_attempts(self):
        print(f"\n{Color.BLUE}Attempts:{Color.OFF}")

        for word in self.word_attempts:
            characters = map(self.char_checker, list(word))
            print("-" * 21)
            print("|", " | ".join(characters), "|")
            print("-" * 21)

        print("\n")

    def play_again(self):
        value = input("Would you like to play again? [y/n]")
        if value.lower() == "y":
            clear()
            self.__init__()
            self.play_game()

        else:
            clear()
            print("Bye!")

    def play_game(self):
        while True:
            clear()
            print(f"Welcome to {Color.GREEN}Wordle{Color.OFF}!")
            self.show_keyboard()

            self.display_attempts()

            attempt = self.take_attempt()
            self.word_attempts.append(attempt)

            # Check which characters are correct


            if attempt and self.word and attempt.lower() == self.word.lower():
                print(f"Yay! You correctly figured out the {Color.GREEN}{attempt.upper()}{Color.OFF}!")
                break

            if len(self.word_attempts) == 6:
                print(f"\nOh No! You didn't manage to figure out the correct word, it was {Color.GREEN}{self.word.upper()}{Color.OFF}")
                return

        self.play_again()

if __name__ == '__main__':
    game = Game()
    game.play_game()
