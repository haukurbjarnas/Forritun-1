string_of_numbers = input()

number_list = []

for num in string_of_numbers.split(","):
    number_list.append(int(num))

print(f"Input list: {number_list}")

print(f"Sorted list: {sorted(number_list)}")

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Check for factors from 3 to the square root of n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
not_prime_list = []

for num in sorted(number_list):
    if is_prime(num) != False:
        not_prime_list.append(num)

print(f"Composite list: {not_prime_list}")

sorted_list = sorted(number_list)
avg_sum = 0 / len(sorted_list)

for num in number_list:
    avg_sum += num


print(f"Min: {sorted_list[0]}, Max: {sorted_list[-1]}, Average: {avg_sum}")