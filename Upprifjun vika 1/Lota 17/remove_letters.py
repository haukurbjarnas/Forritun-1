def remove_letter(input_string, letter_to_remove):
    """Remove a specific letter from a string."""
    cleaned_string = ''.join(char for char in input_string if char != letter_to_remove)
    return cleaned_string

# Example usage:
original_string = "Hello, World!"
letter_to_remove = "o"

result_string = remove_letter(original_string, letter_to_remove)
print("Original string:", original_string)
print(f"String without '{letter_to_remove}':", result_string)
