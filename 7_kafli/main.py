def integer_to_hex(integer_value):
    if integer_value == 0:
        return "0"
    
    hex_characters = "0123456789ABCDEF"
    hex_string = ""
    
    while integer_value > 0:
        remainder = integer_value % 16
        hex_digit = hex_characters[remainder]
        hex_string = hex_digit + hex_string
        integer_value //= 16
    
    return hex_string

# Example usage:
integer_value = int(input(""))
hex_value = integer_to_hex(integer_value)
print(f"The hexadecimal representation of {integer_value} is {hex_value}")








