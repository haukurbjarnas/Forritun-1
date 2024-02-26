a_num = int(input())

while a_num != 1:
    if a_num % 2 == 0:
        a_num = a_num / 2
        print(a_num)
    elif a_num % 2 == 1:
        a_num = (3*a_num) + 1
        print(a_num)