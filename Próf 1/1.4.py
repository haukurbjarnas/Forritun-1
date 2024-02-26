buy_prod = int(input(""))

dollars = int(input(""))

remainder = dollars - buy_prod

if remainder // 20 == 0:
    remainder = remainder - 20
    print("20")

elif remainder // 10 == 0:
    remainder = remainder - 10
    print("10")

elif remainder // 5 == 0:
    remainder = remainder - 5
    print("5")

elif remainder // 2 == 0:
    remainder = remainder - 2
    print("2")

elif remainder // 1 == 0:
    remainder = remainder - 1
    print("1")