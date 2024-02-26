input_file_1 = input()
input_file_2 = input()

file_1 = open(input_file_1, "r")
file_2 = open(input_file_2, "r")

set_1 = set()
set_2 = set()

for line_1, line_2 in zip(file_1, file_2):

    for word_1, word_2 in zip(line_1.split(), line_2.split()):

        set_1.add(word_1)
        set_2.add(word_2)

common_words = list(set_1 & set_2)
not_both = list(set_1 ^ set_2)
only_first = list(set_1 - set_2)

def outcome(a_list):
    bamm_list = []

    for word in a_list:
        bamm_list.append(word.lower())

    sorted_list = sorted(bamm_list)

    if len(a_list) == 1:
        print(f"{sorted_list[0]}.")
    elif len(a_list) == 2:
        print(f"{sorted_list[0]} and {sorted_list[1]}.")
    else:
        for word in sorted_list[0:-1]:
            print(word, end=", ")
        print(f"and {sorted_list[-1]}.")

outcome(not_both)