the_string = input("")

string_list = []
num_list = []

yes = the_string.split()
print(yes)

for i in yes:
    try:
        if int(i) / 1 == int(i):
            num_list.append(int(i))
    except ValueError:
        continue
print(num_list)

needs_list = []
sum = 0

for integer in sorted(num_list):
    if sum == integer:
        continue
    if sum != integer:
        while int(sum) < int(integer):
            if sum in num_list:
                sum += 1
                continue
            needs_list.append(sum)
            sum += 1


print(needs_list)