import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if set(word_to_guess) == set(guessed_letters):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
