password = input("Please enter a password: ")



# listar til að halda yfirliti yfir magni tilrauna og lykilorða þegar stimplað er inn q
tries = []
invalids = []
valids = []
up_sum = 0

while password != "q":
    length = len(password)
    if length > 20 or length < 6:
        print(f"{length}: Invalid length.")
        tries.append(1)
        invalids.append(1)
        password = input("Please enter a password: ")
    for i in password:
        if i == i.upper():
            up_sum += 1
        if up_sum == 0:
            tries.append(1)
            invalids.append (1)
            print("Missing upper case letter")
            password = input("Please enter a password: ")
    for i in password:
        low_sum = 0
        if i == i.lower():
            low_sum += 1
        if low_sum == 0:
            tries.append(1)
            invalids.append(1)
            print("Missing lower case letter")
            password = input("Please enter a password: ")
