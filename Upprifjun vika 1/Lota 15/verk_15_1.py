a_set = set()

amount = int(input())

while amount > 0:
    a_chore = input()
    if a_chore in a_set:
        pass
    else:
        a_set.add(a_chore)
    amount -= 1

for i in a_set:
    print(i)