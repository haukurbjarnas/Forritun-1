import string

def remove_punctuation(input_string):
    # Creating a translation table to remove punctuations
    translator = str.maketrans("", "", string.punctuation)

    # Removing all punctuations in the string
    cleaned_string = input_string.translate(translator)

    return cleaned_string

# Example usage:
user_input = input("Enter a string with punctuations: ")
result = remove_punctuation(user_input)

print("String without punctuations:", result)
