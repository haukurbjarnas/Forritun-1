def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check for factors from 3 to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Example usage:
number_to_check = 4

if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
