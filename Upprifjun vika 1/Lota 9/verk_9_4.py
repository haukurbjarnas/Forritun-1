a_file = input()

file = open(a_file, "r")

for line in file:
    print("".join(reversed(line)))

