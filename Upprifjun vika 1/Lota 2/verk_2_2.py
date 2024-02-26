a_num = int(input())
b_num = int(input())
c_num = int(input())

if a_num > b_num and a_num > c_num:
    print(a_num)
elif b_num > a_num and b_num > c_num:
    print(b_num)
elif c_num > a_num and c_num > b_num:
    print(c_num)