my_int = int(input(""))

number = 1

divisor = 0

sum = 0

for i in range (my_int):
    divisor = number / 2
    number = divisor
    sum += divisor
    print(sum)