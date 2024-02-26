# m = fjölda vöruverða

# t = heildarverð varanna

# l = lægsta verðið

my_int = float(input(""))

lowest_list = []

number_of_prices = 0

my_sum = 0

if my_int == 0:
    print(f"Number of items: 0")
    print(f"Total price: 0.0")

while my_int != 0:
    number_of_prices += 1
    my_sum += my_int
    if my_int != 0:
        lowest_list.append(my_int)
    my_int = float(input(""))

list_sum = sum(lowest_list)

total_round = round(my_sum, 2)

if number_of_prices != 0:
    print(f"Number of items: {number_of_prices}")
if my_sum != 0:
    print(f"Total price: {total_round}")
if list_sum != 0:
    print(f"Lowest price: {min(lowest_list)}")