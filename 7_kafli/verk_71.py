def precedes(one_string, another_string) -> str:
    lower_1 = one_string.lower()
    lower_2 = another_string.lower()
    if lower_1 > lower_2:
        return another_string
    elif lower_1 < lower_2:
        return one_string
    elif lower_1 == lower_2:
        return one_string
