import math

stop_range = int(input(""))

num_divisors = int(input(""))

if stop_range < 20 or stop_range > 100:
    print("Invalid number!")
    stop_range = int(input(""))

if num_divisors < 1 or num_divisors < 12:
    print("Invalid number")
    num_divisors = int(input(""))

#koma í veg fyrir að hægt sé að stimpla inn vitlaust input

the_list = []

i = 0
new_i = 0

for i in range (20, stop_range+1):
    for j in range (i):
        if i == len(2):
            