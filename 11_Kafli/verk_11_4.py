my_input = input("")

the_list = my_input.split()

int_list = []

for i in the_list:
    int_list.append(float(i))

if len(the_list) < 3:
    print("At least 3 scores needed!")
    exit()


int_list.sort()
int_list.pop(0)
int_list.pop(0)
int_list.pop(0)

sum = 0

for i in int_list:
    sum += i

print(f"Sum of scores (3 lowest removed): {round(sum, 1)}")