def open_file():
    a_file = input()
    try:
        file = open(a_file, "r")
    except FileNotFoundError:
        exit()

    return file


def reading_file(file):

    a_dict = dict()

    for line in file:

        first_name, last_name, throw = line.split(" ")

        full_name = first_name + " " + last_name

        splitted_throw = throw.split("\n")

        if full_name in a_dict:
            a_dict[full_name].add(splitted_throw[0])

        else:
            a_dict[full_name] = {splitted_throw[0]}

    return a_dict

def finding_average(a_dict):

    average_dict = dict()

    for keys, values in zip(a_dict.keys(), a_dict.values()):

        if len(values) > 1:
            average = sum(values) / len(values)
            average_dict[keys] = average

    highest_average = 0
    name = 0
    
    for keys, values in zip(a_dict.keys(), a_dict.values()):
        highest_average(max(values))
        