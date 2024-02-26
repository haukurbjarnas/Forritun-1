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
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            if i == i.upper():
                list += i.lower()
            if i == i.lower():
                list += i.upper()
        if (ord(i) >= 48 and ord(i) <= 57):
            list += i
    return list

def to_hex(an_int):
    if an_int == 0:
        return "0"
    hex_characters = "0123456789ABCDEF"
    hex_string = ""
    while an_int > 0:
        remainder = an_int % 16
        hex_digit = hex_characters[remainder]
        hex_string = hex_digit + hex_string
        an_int //= 16
    return hex_string

my_string = input("")

while my_string != "q":
    if my_string == "c":
        new_string = str(input(""))
        dig_func = collect_digits(new_string)
        print(dig_func)
    if my_string == "i":
        newer_string = str(input(""))
        inverse_func = inverse_case(newer_string)
        print(inverse_func)
    if my_string == "h":
        hex_input = int(input(""))
        return_hex = to_hex(hex_input)
        print(return_hex)
    my_string = input("")