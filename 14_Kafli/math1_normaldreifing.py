import math

def heildun (x):
    calc = math.e**-1/2*((x-100)/15)**2
    return calc

input_a = 95

input_b = 120

calculation = 1/(math.sqrt(2)*math.pi*15)*(heildun(input_b)-heildun(input_a))

print(round(calculation, 4))