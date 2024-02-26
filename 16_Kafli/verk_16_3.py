class Hangman:

    def __init__(self, word: str):
        self.word = word.upper()
        self.displayword = "_" * len(self.word)

    def guess_letter(self, letter: str) -> bool:
        self.letter = letter
        self.incorrect_guesses = 0
        letter_list = []
        for stafur in self.word:
            letter_list.append(stafur)
        if self.letter in letter_list:
            return True
        else:
            self.incorrect_guesses += 1
            return False

    def __str__(self):
        return f"Number of incorrect guesses: {self.incorrect_guesses}"