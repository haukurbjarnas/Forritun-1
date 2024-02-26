
MIN_LEN = 6
MAX_LEN = 20
QUIT = "q"


password_count = 0
valid_count = 0
invalid_count = 0

while True:
    password = input()

    
    if password == QUIT:
        break

    password_count += 1

    has_lower = False
    has_upper = False
    has_digit = False

    
    if MIN_LEN <= len(password) <= MAX_LEN:
        
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True

        
        if has_lower and has_upper and has_digit:
            valid_count += 1
            print(f"{password}: Valid password of length {len(password)}.")
        else:
            invalid_count += 1
            if not has_lower:
                print(f"{password}: Missing lower case letter.")
            if not has_upper:
                print(f"{password}: Missing upper case letter.")
            if not has_digit:
                print(f"{password}: Missing numeric letter.")
    else:
        invalid_count += 1
        print(f"{password}: Invalid length.")


print(f"You tried {password_count} passwords, {valid_count} valid, {invalid_count} invalid.")