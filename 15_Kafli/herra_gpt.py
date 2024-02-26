# Sample dictionary with keys and values
data = {
    "key1": ["apple", "banana", "cherry"],
    "key2": ["orange", "grape", "kiwi"],
    "key3": ["strawberry", "blueberry", "raspberry"]
}

# Word to search for
search_word = "orange"

# Initialize a list to store keys that contain the search word
matching_keys = []

# Loop through the dictionary
for key, values in data.items():
    if search_word in values:
        matching_keys.append(key)

# Print the keys that contain the search word
if matching_keys:
    print(f"The word '{search_word}' was found in the following keys:")
    for key in matching_keys:
        print(key)
else:
    print(f"The word '{search_word}' was not found in any keys.")
