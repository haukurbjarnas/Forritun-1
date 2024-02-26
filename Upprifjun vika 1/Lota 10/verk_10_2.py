amount = int(input())

num_list = []

while amount > 0:
    a_num = int(input())
    num_list.append(a_num)
    amount -= 1

sorted_list = sorted(num_list)

check = -1

for num in sorted_list:
    print(sorted_list[check])
    check = check - 1