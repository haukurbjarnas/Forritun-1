password = input("Please enter a password: ")

invalids = []

valids = []

tries = []

while password != "q":
    pass_length = len(password)
    if pass_length < 6 or pass_length > 20:
        print(f"{pass_length}: Invalid length.")
        invalids.append(1)
        tries.append(1)
        password = input("Please enter a password: ")
    for i in password:
            upper_checker = 0
            if i != i.upper():
                upper_checker += 1
            if upper_checker != 0:
                print("Missing upper case letter.")
                password = input("Please enter a password: ")
    for i in password:
            lower_checker = 0
            if i != i.lower():
             lower_checker += 1
            if lower_checker != 0:
             print("Missing lower case letter.")
             password = input("Please enter a password: ")

   


print(f"You tried {len(tries)} passwords, {len(valids)} valid, {len(invalids)} invalid.")