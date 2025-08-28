import random

# List of words to guess
words = ["python", "programming", "developer", "hangman", "challenge", "artificial", "intelligence"]

# Hangman stages (visuals)
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(words).upper()

def play_game():
    word = choose_word()
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")

    while wrong_guesses < max_wrong and "_" in guessed_word:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_wrong - wrong_guesses} tries left.")

    # Final result
    print(HANGMAN_PICS[wrong_guesses])
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print(" Game Over! The word was:", word)

if __name__ == "__main__":
    play_game()
