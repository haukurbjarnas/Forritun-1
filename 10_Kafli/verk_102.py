the_range = int(input(""))

the_list = []

print_list = []

x = -1

for i in range(the_range):
    your_num = int(input(""))
    the_list.append(your_num)

for j in the_list:
    print_list.append(the_list[x])
    x += -1

for h in print_list:
    print(h, end=" ")