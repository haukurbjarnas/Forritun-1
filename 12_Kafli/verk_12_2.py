enter_a_file = input("")

checker = 0

while checker != 1:
    num_list = []
    
    try:
        file = open(enter_a_file, "r")
        for line in file:
            line_check = line.split()
            for word in line_check:
                try:
                    word = int(word)
                    num_list.append(int(word))
                except:
                    ValueError
                    continue
        print(sorted(num_list))
        checker += 1
    
    except FileNotFoundError:
        print(f"{enter_a_file} not found! Please try again.")
        enter_a_file = input("")