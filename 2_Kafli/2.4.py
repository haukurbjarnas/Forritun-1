a = int(input(""))
b = int(input(""))
c = int(input(""))

power_b = b**2

a_c = a * c

d = power_b - (4*a_c)

if d > 0:
    print("2")
elif d == 0:
    print("1")
else:
    print("0")