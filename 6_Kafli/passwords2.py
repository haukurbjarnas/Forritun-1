QUIT = "q"
MIN = 6
MAX = 20

attempts = 0
valids = 0
invalids = 0

while True:
    password = input("")

    if password == QUIT:
        break

    attempts += 1

    has_lower = False
    has_upper = False
    has_digit = False

    if MIN <= len(password) >= MAX:
        for i in password:
            if i.isupper():
                has_upper = True
            elif i.islower():
                has_lower = True
            elif i.isdigit():
                has_digit = True
            
        if has_digit and has_lower and has_upper:
            valids += 1
            print(f"{password}: Valid password of length {len(password)}.")
        else:
            invalids += 1
            if not has_lower:
                print(f"{password}: Missing lower letter.")
            if not has_upper:
                print(f"{password}: Missing upper letter.")
            if not has_digit:
                print(f"{password}: Missing numeric letter.")
    else:
        invalids += 1
        print(f"{password}: Invalid length.")

print(f"You tried {attempts} passwords, {valids} valid, {invalids} invalid.")
