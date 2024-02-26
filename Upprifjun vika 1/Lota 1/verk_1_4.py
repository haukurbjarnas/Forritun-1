import math

int_a = int(input())
int_b = int(input())
int_c = int(input())

s = (int_a+int_b+int_c)/2

big_a = math.sqrt(s*(s-int_a)*(s-int_b)*(s-int_c))

print(big_a)