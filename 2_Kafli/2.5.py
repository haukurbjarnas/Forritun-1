elo_input = int(input(""))

if elo_input >= 2700:
    print("Super grandmaster")
elif elo_input >= 2500:
    print("Grandmaster")
elif elo_input >= 2400:
    print("International grandmaster")
elif elo_input < 2400:
    print("Amateur")
elif elo_input <= 999:
    print("Invalid")