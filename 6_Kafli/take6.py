password = str(input(""))

attempts = []
invalids = []
valids = []

while password != "q":
    pass_len = len(password)
    upsum = 0
    lowsum = 0
    numsum = 0
    secret = 0
    if pass_len < 6 or pass_len > 20:
        print(f"{password}: Invalid length.")
        attempts.append(1)
        secret += 1
        password = str(input(""))
        continue
    for i in password:
        order66 = ord(i)
        if order66 > 61 and order66 < 122:
            lowsum += 1
    if lowsum == 0:
            print(f"{password}: Missing lower case letter.")
            attempts.append(1)
            secret += 1
    for i in password:
        order66 = ord(i)
        if order66 > 48 and order66 < 57:
         numsum += 1
    if numsum == 0:
         print(f"{password}: Missing numeric letter.")
         attempts.append(1)
         secret += 1
    for i in password:
        order66 = ord(i)
        if order66 > 41 and order66 < 90:
            upsum += 1
    if upsum == 0:
            print(f"{password}: Missing upper case letter.")
            attempts.append(1)
            secret += 1
    if secret == 0:
         print(f"Valid password of length {pass_len}.")
         attempts.append(1)
         valids.append(1)
    password = str(input(""))
    continue

invalids = len(attempts) - len(valids)

print(f"You tried {len(attempts)} passwords, {len(valids)} valid, {invalids} invalid.")