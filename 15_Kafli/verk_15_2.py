import string

text_file_1 = input()
text_file_2 = input()
file_1 = open(text_file_1, "r")
file_2 = open(text_file_2, "r")

file_set_1 = set()
file_set_2 = set()

backup_list1 = []
backup_list2 = []

def and_stuff (a_list):
    result = ""
    for i, word in enumerate(a_list):
        result += word

        if i < len(a_list) - 1:
            result += ", "
        
        if i == len(a_list) - 2:
            result = result.rstrip(", ") + " and "
    if len(a_list) >= 2:
        result += "."
    return result

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation.replace("-", ""))
    cleaned_text = input_string.translate(translator)
    return cleaned_text

for line in file_1:
    new_line = line.split()
    for word in new_line:
        file_set_1.add(remove_punctuation(word))
        backup_list1.append(remove_punctuation(word))

for line in file_2:
    new_line = line.split()
    for word in new_line:
        file_set_2.add(remove_punctuation(word))
        backup_list2.append(remove_punctuation(word))

result = ""

combined_set = file_set_1.intersection(file_set_2)
combined_list = sorted(list(combined_set))

symmetra = file_set_1.symmetric_difference(file_set_2)
symmetra_list = sorted(list(symmetra))

first_not_second = file_set_1.difference(file_set_2)
first_not_list = sorted(list(first_not_second))

print(f"The two files have {len(combined_list)} words in common.")
print("These words are as follows:")
print(and_stuff(combined_list))

print(f"There are {len(symmetra_list)} words that are only in either file but not both.")
print("These words are as follows:")
print(and_stuff(symmetra_list))

print(f"There are {len(first_not_list)} words that only appear in the first file.")
print("These words are as follows:")
print(and_stuff(first_not_list))