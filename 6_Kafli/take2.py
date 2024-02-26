password = input("Please enter a password: ")

tries = []

valids = []

invalids = []


while password != "q":
    pass_length = len(password)
    if pass_length < 6 or pass_length > 20:
        invalids.append(1)
        print(f"{password}: Invalid length.")
    for i in password:
        upper_sum = 0
        if i != i.upper():
            upper_sum += 1
            if upper_sum == 0:
                print("Missing upper case letter.")
    tries.append(1)
    password = input("Please enter a password: ")

print(f"You tried {len(tries)} passwords, {len(valids)} valid, {len(invalids)} invalid.")