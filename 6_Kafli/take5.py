password = str(input(""))

attempts = []
valids = []
invalids = []

while password != "q":
    pass_len = len(password)
    up_sum = 0
    low_sum = 0
    num_sum = 0
    secret = 0
    if pass_len < 6 or pass_len > 20:
        print(f"{password}: Invalid length.")
        password = str(input(""))
        attempts.append(1)
        invalids.append(1)
        continue
    for i in password:
        order66 = ord(i)
        if order66 > 41 and order66 < 90:
            up_sum += 1
    if up_sum == 0:
        print(f"{password}: Missing upper case letter.")
        attempts.append(1)
        invalids.append(1)
    for i in password:
        order66 = ord(i)
        if order66 > 97 and order66 < 122:
            low_sum += 1
    if low_sum == 0:
        print(f"{password}: Missing lower case letter.")
        attempts.append(1)
        invalids.append(1)
    for i in password:
        if order66 > 48 and order66 < 57:
            num_sum += 1
    if num_sum == 0:
        print(f"{password}: Missing numeric letter.")
        attempts.append(1)
        invalids.append(1)
    else:
        print(f"{password}: Valid password of length {len(password)}.")
        attempts.append(1)
        valids.append(1)
    password = str(input(""))
    continue

print(f"You tried {len(attempts)} passwords, {len(valids)} valid, {len(invalids)} invalid.")