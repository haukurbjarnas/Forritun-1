import math

x_1 = int(input(""))
y_1 = int(input(""))
x_2 = int(input(""))
y_2 = int(input(""))

power_x = (x_2 - x_1)**2

power_y = (y_2 - y_1)**2

power_sum = power_x + power_y


root = math.sqrt(power_sum)

print(root)