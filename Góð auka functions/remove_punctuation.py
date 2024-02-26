import string

def remove_punctuation(input_string):
    """Remove punctuation from a string."""
    translator = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string

# Example usage:
original_string = "Hello, World! This is an example."

cleaned_string = remove_punctuation(original_string)
print("Original string:", original_string)
print("Cleaned string:", cleaned_string)
