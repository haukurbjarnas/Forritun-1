k_num = int(input())

n_num = int(input())

power_list = []

for i in range(n_num):
    x_num = int(input())
    power_list.append(x_num)

sum = 0

for i in power_list:
    sum += k_num**i

print(sum)