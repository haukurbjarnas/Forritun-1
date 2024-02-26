my_int = int(input(""))

even_number = 0

odd_number = 0

while my_int != 1:
    if my_int % 2 == 0:
        even_number = my_int / 2
        print(even_number)
        my_int = even_number
    elif my_int % 3 == 0:
        odd_number = 3 * my_int + 1
        print(odd_number)
        my_int = odd_number
    