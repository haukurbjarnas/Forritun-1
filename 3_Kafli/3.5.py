pip_int = int(input("Enter a number bitch!: "))

while pip_int != 0:
    pip_division = pip_int / 10
    if pip_division // 7 == 0:
        print("The number does contain 7.")
        exit()

print("The number does not contain 7.")