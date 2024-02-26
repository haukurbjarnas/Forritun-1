a_input = input()

amount_of_bags, the_bag = a_input.split()

num_list = []

amount_of_bags = int(amount_of_bags)

while int(amount_of_bags) > 0:
    other_bag = input()
    num_list.append(int(other_bag))
    amount_of_bags -= 1

sort_list = sorted(num_list)

check = 1

what_order = 0

for num in sort_list:
    if num == int(the_bag):
        what_order = check
    check += 1

if check == 1:
    print("fyrst")
elif check == 2:
    print("naestfyrst")
else:
    print(f"{check} fyrst")