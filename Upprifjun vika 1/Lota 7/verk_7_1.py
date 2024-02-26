def precedes(one_string, another_string):

    pot_1 = 0
    pot_2 = 0
    
    for letter_1, letter_2 in zip(one_string.lower(), another_string.lower()):
        if ord(letter_1) > ord(letter_2):
            pot_1 += 1
        elif ord(letter_2) > ord(letter_1):
            pot_2 += 1
        elif ord(pot_1) == ord(pot_2):
            pass

    if pot_1 > pot_2:
        return one_string
    elif pot_2 > pot_1:
        return another_string
    


print(precedes("haukur", "duna"))