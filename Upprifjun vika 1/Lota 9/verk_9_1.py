def is_float(string_to_test):

    try:
        if float(string_to_test) / 1 == float(string_to_test):
            return True
    except ValueError:
        return False
    

print(is_float("3e"))