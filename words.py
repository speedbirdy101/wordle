class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# a trie should have a root node:
root = Node()


def insert_word(word):
    current = root

    for char in word:
        if char not in current.children:
            current.children[char] = Node()

        current = current.children[char]

    current.is_end_of_word = True


def search_word(word):
    current = root

    for char in word.upper():
        if char not in current.children:
            return False

        current = current.children[char]

    return current.is_end_of_word
