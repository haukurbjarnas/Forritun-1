def sum_of_divisors(number):
    
    num_sum = 1

    for num in range(1, number):
        if number % num == 0:
            num_sum += num
    
    if num_sum > number:
        return f"{number} is abundant."
    elif num_sum < number:
        return f"{number} is deficient."
    elif num_sum == number:
        return f"{number} is a perfect number."
    
print(sum_of_divisors(10))