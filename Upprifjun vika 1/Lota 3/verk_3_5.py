a_num = int(input())

check = 0

while a_num != 0:
    if a_num % 10 == 7:
        check = 0
    a_num = a_num / 10

if check > 0:
    print("The number contains 7")
else:
    print("The number does not contain 7")