stop_range = int(input(""))
num_divisors = int(input(""))

divisor_list = []


for i in range(20, stop_range):
    tens_digit = i // 10
    ones_digit = i % 10
    sum_of_digits = tens_digit + ones_digit
    sum_of_digits_squared = (sum_of_digits**2)
    if sum_of_digits_squared == i:
        print(i)
    i += 1

h = 1

for j in range (stop_range):
    if j % h == 0:
        h += 1
        if h == num_divisors:
            new_j = str(j)
            divisor_list.append(new_j)

print(divisor_list)



