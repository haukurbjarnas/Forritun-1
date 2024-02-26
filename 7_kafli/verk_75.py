def sum_of_divisors(number):
    range_num = number
    og_num = number
    for i in range (1, range_num):
        modulo = number % i
        if modulo == 0:
            number += i
        i += 1
    number = number - og_num
    return number

def decide(number):
    comparison = 
    checker = sum_of_divisors(number)
    if checker > number:
        return f"{number} is abundant."
    elif checker < number:
        return f"{number} is deficient."
    else:
        return f"{number} is a perfect number."

