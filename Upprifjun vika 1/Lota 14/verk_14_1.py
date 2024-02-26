def keys_and_values():
    question = ""
    a_dict = dict()
    while question != "n":
        the_key = input()
        the_value = input()
        a_dict[the_key] = the_value
        question = input()
    return a_dict

def outcome(dictionary):
    print("")
    for key, value in zip(dictionary.keys(), dictionary.values()):
        print(f"{key}:")
        print(f"{value:>4}")
        print("")


global_dict = keys_and_values()

outcome(global_dict)