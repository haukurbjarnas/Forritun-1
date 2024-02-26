password = str(input(""))

attempts = []
valids = []
invalids = []

while password != "q":
    password_len = len(password)
    low_sum = 0
    up_sum = 0
    num_sum = 0
    for i in password:
        order66 = ord(i)
        if order66 >= 48 and order66 <= 57:
            num_sum += 1
        if order66 >= 65 and order66 <= 90:
            up_sum += 1
        if order66 >= 96 and order66 <= 122:
            low_sum += 1
    if low_sum > 0 and num_sum > 0 and up_sum > 0:
        print(f"{password}: Valid password of length {password_len}.")
        attempts.append(1)
        valids.append(1)
        password = str(input(""))
        continue
    if password_len < 6 or password_len > 20:
        print(f"{password}: Invalid length.")
        attempts.append(1)
        invalids.append(1)
        password = str(input(""))
        continue
    for i in password:
        order66 = ord(i)
        if order66 >= 97 and order66 <= 122:
            low_sum += 1
    if low_sum == 0:
        print(f"{password}: Missing lower case letter.")
    for i in password:
        order66 = ord(i)
        if order66 >= 65 and order66 <= 90:
            up_sum += 1
    if up_sum == 0:
        print(f"{password}: Missing upper case letter.")
    for i in password:
        order66 = ord(i)
        if order66 >= 48 and order66 <= 57:
            num_sum += 1
    if num_sum == 0:
        print(f"{password}: Missing numeric letter.")
    attempts.append(1)
    invalids.append(1)
    password = str(input(""))
    continue

print(f"You tried {len(attempts)} passwords, {len(valids)} valid, {len(invalids)} invalid.")