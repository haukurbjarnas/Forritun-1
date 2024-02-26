def sum_of_divisors(number):
    sum = 0
    for i in range (1, number):
        modulo = number % i
        if modulo == 0:
            sum += i
        i += 1
    return number and sum
    
def decide(number):
    my_num = sum_of_divisors(number)
    perfect = f"{number} is a perfect number."
    defficient = f"{number} is deficient."
    abundant = f"{number} is abundant."
    if sum > number:
        return abundant
    elif sum < number:
        return defficient
    else:
        return perfect