buy_prod = int(input(""))

amount_cash = int(input(""))

change = amount_cash - buy_prod

# dollarar eru 20, 10, 5, 2, 1

while change >= 1:
    if change >= 20:
        change = change - 20
        print("20")
    if 20 > change and change >= 10:
        change = change - 10
        print("10")
    if 10 > change and change >= 5:
        change = change - 5
        print("5")
    if 5 > change and change >= 2:
        change = change - 2
        print("2")
    if 2 > change and change >= 1:
        change = change -1
        print("1")
