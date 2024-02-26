word = input()



back = reversed(word)

if list(word) == list(back):
    print("Palindrome!")
else:
    print("Nothing special about this word...")