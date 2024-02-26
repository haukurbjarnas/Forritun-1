check = 0
length = 10

while check == 0:
    choice = input(f"Is Sváfnir's cock bigger than {length} cm? (Y)es or (N)o: ")
    choice = choice.lower()
    if choice == "y":
        length += 1
    if choice == "n":
        check += 1

print(f"Wow! Sváfnir's cock is {length} centimeters! Thats pretty huge")