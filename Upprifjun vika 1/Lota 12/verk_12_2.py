a_file = input()

chica = 0


while chica == 0:
    try:
        file = open(a_file, "r")
        chica += 1


    except FileNotFoundError:
        print(f"{a_file} not found! Please try again.")
    
    a_file = input()

num_list = []

for line in file:

    for word in line.split():
        try:
            if int(word) / 1 == int(word):
                num_list.append(word)
        
        except ValueError:
            continue

print(num_list)