from itertools import permutations
from typing import Set


def generate_words(characters: list[str]) -> Set[str]:
    words: Set[str] = set()
    for i in range(1, len(characters) + 1):
        perms = permutations(characters, i)
        for perm in perms:
            word = ''.join(perm)
            words.add(word)
    return words


def main():
    input_characters = input("Enter characters separated by commas: ").split(',')
    input_characters = [char.strip() for char in input_characters]
    possible_words = generate_words(input_characters)
    print("Possible words:", possible_words)


if __name__ == "__main__":
    main()
