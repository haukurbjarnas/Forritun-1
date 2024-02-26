budget = int(input(""))
cloud = int(input(""))
equatorial = int(input(""))
elevator = int(input(""))

sum = cloud + equatorial + elevator

if budget > sum or budget == sum:
    print("The budget is sufficient")
else:
    print("The budget is unsufficient")