def collect_digits(a_str):
    new_string = ""
    for i in a_str:
        order66 = ord(i)
        if order66 >= 48 and order66 <= 57:
            new_string += i
    return new_string

def inverse_case(a_str):
    list = ""
    for i in a_str:
        if i == i.upper():
            list += i.lower()
        if i == i.lower():
            list += i.upper()
    return list

def to_hex(an_int):
    if an_int == 0:
        return "0"  
    hex_characters = "0123456789ABCDEF"
    hex_str = ""
    while an_int > 0:
        remainder = an_int % 16
        hex_digit = hex_characters[remainder]
        hex_str = hex_digit + hex_str
        an_int //= 16
    return hex_str