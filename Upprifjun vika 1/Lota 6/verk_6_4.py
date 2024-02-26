sentence = input()

for word in sentence:
    for letter in word:
        if letter == letter.upper():
            print(letter.lower(), end="")
        elif letter == letter.lower():
            print(letter.upper(), end="")
        else:
            print(letter, end="")