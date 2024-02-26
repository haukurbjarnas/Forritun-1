len_num = int(input(""))

square_list = []

i = 1

sum = 1

for i in range(len_num):
    list_num = sum **2
    square_list.append(list_num)
    sum += 1

print(square_list)