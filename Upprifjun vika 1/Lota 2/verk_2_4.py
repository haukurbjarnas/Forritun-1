a_num = int(input())
b_num = int(input())
c_num = int(input())
d_num = (b_num**2)-4*(a_num*c_num)

if d_num > 0:
    print(2)
elif d_num == 0:
    print(1)
elif d_num < 0:
    print(0)