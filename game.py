import os
from color import Color
import random
from words import *


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

        self.keyboard_bar_len = len(self.alphabet) * 2

    def random_word(self):
        with open("words.txt") as file:
            words = file.read().splitlines()
            random_line = random.randint(0, len(words))
            self.word = words[random_line].upper()

            # Create the tree
            for word in words:
                insert_word(word.upper())

    def char_checker(self, char):
        return f"{self.characters[char]}{char}{Color.OFF}"

    def show_keyboard(self):
        print(f"{'__' * self.keyboard_bar_len}")
        print(
            " " + " | ".join(
                map(self.char_checker, self.characters)
            )
        )
        print(f"{'--' * self.keyboard_bar_len}\n")

    def incorrect_attempt(self, msg):
        clear()
        self.show_keyboard()
        self.display_attempts()
        print(f"{Color.RED}{msg}, please try again{Color.OFF}")

        return self.take_attempt()

    def take_attempt(self):
        attempt = input("Please enter a word to try: [5 letters only]\n")

        # Validify the attempt
        if len(attempt) != 5:
            return self.incorrect_attempt("Not 5 letters")

        if not attempt.isalpha():
            return self.incorrect_attempt("Must only contain letters")

        if not search_word(attempt):
            return self.incorrect_attempt("Word does not exist")

        return attempt

    def update_keyboard_colours(self, attempt):
        for index, char in enumerate(attempt):
            if char not in self.word:
                if char in self.characters:
                    # Make it grey
                    # self.characters[char] = Color.GREY

                    self.characters.pop(char)
                    self.keyboard_bar_len = len(self.characters) * 2

            elif index == self.word.index(char):
                self.characters[char] = Color.GREEN

            else:
                if self.characters[char] != Color.GREEN:
                    self.characters[char] = Color.YELLOW

    def colour_word(self, word):
        list_word = []
        for index, char in enumerate(word):
            if char not in self.word:
                list_word.append(
                    f"{Color.GREY}{char}{Color.OFF}"
                )

            elif index == self.word.index(char):
                list_word.append(
                    f"{Color.GREEN}{char}{Color.OFF}"
                )

            else:
                list_word.append(
                    f"{Color.YELLOW}{char}{Color.OFF}"
                )

        return list_word

    def display_attempts(self):
        print(f"\n{Color.BLUE}Attempts:{Color.OFF}")

        for word in self.word_attempts:
            print("-" * 21)
            print("|", " | ".join(self.colour_word(word)), "|")
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

            attempt = self.take_attempt().upper()
            self.word_attempts.append(attempt)
            self.update_keyboard_colours(attempt)

            if attempt and self.word and attempt == self.word:
                print(f"Yay! You correctly figured out the {Color.GREEN}{attempt}{Color.OFF}!")
                break

            if len(self.word_attempts) == 6:
                print(f"\nOh No! You didn't manage to figure out the correct word, it was {Color.GREEN}{self.word}{Color.OFF}")
                break

        self.play_again()
