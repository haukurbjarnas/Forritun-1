number_of_chores = int(input(""))

chore_list = []
chore_set = set()


while number_of_chores > 0:
    chores = input()
    if chores in chore_set:
        pass
    else:
        chore_set.add(chores)
        print(chores)
    number_of_chores -= 1

