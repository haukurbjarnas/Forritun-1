def main():
    info_file = input("")
    number_of_word = int(input(""))

    secret_word = finding_the_word(info_file, number_of_word)

    attempts = 1
    guessed_letters = []

    while attempts <= 12:
        print(f"Secret word: {display_word(secret_word, guessed_letters)}")
        print(f"Guess {attempts}/12")
        guess = input("")
        if guess in secret_word:
            guessed_letters.append(guess)
            print(f"Correct letter {guess}!")
            attempts += 1
            if set(secret_word) == set(guessed_letters):
                print(f"Secret word: {display_word(secret_word, guessed_letters)}")
                print("You won!")
                exit()
        else:
            print(f"Incorrect letter {guess}!")
            attempts += 1
    print(f"Secret word: {display_word(secret_word, guessed_letters)}")
    print(f"You lost! The secret word was {secret_word}")


def finding_the_word (file_line, line_num):
        try:
            file = open(file_line, "r")
        except FileNotFoundError:
            exit()
        line_check = 1

        for line in file:
            if line_check == line_num:
                secret_word = line.strip("\n")
                line_check += 1
            else:
                line_check += 1
        return secret_word

def display_word (secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "-" + " "
    return display

main()