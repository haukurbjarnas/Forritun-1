a_sentence = input()
a_letter = input()

word_list = []
word_check = 0

for word in a_sentence:
    for letter in word:
        word_list.append(letter)

for letter in word_list:
    if letter == a_letter:
        print(word_check)
    word_check += 1