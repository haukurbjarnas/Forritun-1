my_int = int(input(""))

if my_int % 4 != 0:
    if my_int % 100 == 0:
        if my_int % 400 == 0:
            print("Leap year")

