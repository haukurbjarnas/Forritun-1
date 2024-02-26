def is_valid_password(password):
    password_len = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if 6 <= password_len <= 20 and has_lower and has_upper and has_digit:
        return True
    else:
        return False

attempts = []
valids = []
invalids = []

while True:
    password = input("Enter a password (or 'q' to quit): ")

    if password == "q":
        break

    if is_valid_password(password):
        print(f"{password}: Valid password of length {len(password)}.")
        valids.append(password)
    else:
        print(f"{password}: Invalid password.")
        invalids.append(password)

    attempts.append(password)

print(f"You tried {len(attempts)} passwords, {len(valids)} valid, {len(invalids)} invalid.")