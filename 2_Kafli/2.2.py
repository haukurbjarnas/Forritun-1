int_a = int(input(""))
int_b = int(input(""))
int_c = int(input(""))

if int_a > int_b and int_a > int_c:
    print(int_a)
elif int_b > int_a and int_b > int_c:
    print(int_b)
else:
    print(int_c)