def divide_safe(num1_str, num2_str):

    try:
        result = float(num1_str) / float(num2_str)
        return round(result, 5)
    except ValueError or ZeroDivisionError:
        return None
    

print(divide_safe("3.87", "37.242b"))