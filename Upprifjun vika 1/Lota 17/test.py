a_string = "Haukur Bjarnason"

def remove_letter(input_string, letter_to_remove):
    """Remove a specific letter from a string."""
    cleaned_string = ''.join(char for char in input_string if char != letter_to_remove)
    return cleaned_string

new_string = remove_letter(a_string, "\n")

print(new_string)