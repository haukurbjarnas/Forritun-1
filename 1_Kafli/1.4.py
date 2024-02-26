import math

int_a = int(input("Enter number A: "))
int_b = int(input("Enter number B: "))
int_c = int(input("Enter number C: "))

int_s = (int_a + int_b + int_c) / 2

s_a = int_s - int_a
s_b = int_s - int_b
s_c = int_s - int_c

root = math.sqrt(int_s*s_a*s_b*s_c)

print(root)