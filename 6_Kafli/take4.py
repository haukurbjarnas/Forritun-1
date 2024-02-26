attempts = []

password = (input(""))

valids = []
invalids = []

secret = 0


while password != "q":
    up_sum = 0
    down_sum = 0
    num_sum = 0
    pass_len = len(password)
    if pass_len < 6 or pass_len > 20:
        print(f"{password}: Invalid length.")
        invalids.append(1)
        secret += 1
        password = str(input(""))
        attempts.append(1)
        continue
    for i in password:
        if i == i.upper():
            up_sum += 1
    if up_sum == 0:
        print(f"{password}: Missing upper case letter.")
        invalids.append(1)
        secret += 1
    for i in password:
        if i == i.lower():
            down_sum += 1
    if down_sum == 0:
        print(f"{password}: Missing lower case letter.")
        invalids.append(1)
        secret += 1
    for j in password:
        if ord(j) > 48 and ord(j) < 57:
            num_sum += 1
    if num_sum == 0:
        print(f"{password}: Missing numeric letter.")
        invalids.append(1)
        secret += 1
    if password == int(password):
        print(f"{password}: Missing upper case letter.")
        print(f"{password}: Missing lower case letter.")
        secret += 1
    if secret == 0:
        print(f"{password}: Valid password of length {pass_len}.")
        valids.append(1)
        secret += 1
    password = (input(""))
    attempts.append(1)
    continue

the_invalids = len(attempts) - len(valids)

print(f"You tried {len(attempts)} passwords, {len(valids)} valid, {the_invalids} invalid.")