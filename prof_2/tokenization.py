input_file = input("")

file = open(input_file, "r")

word_count = []

for line in file:
    new_line = line.split()
    for word in new_line:
        word_count.append(word)

print(len(word_count))

open_again = open(input_file, "r")

for new_line in open_again:
    newer_liner = new_line.split()
    for worder in newer_liner:
        print(worder)

open_once_more = open(input_file, "r")

for lína in open_once_more:
    ný_lína = lína.split()
    for orð in ný_lína:
        for stafur in orð:
            sum = 0
            try:
                if ord(stafur) >= 33 and ord(stafur) <= 47:
                    length = len(orð) - 1
                    print(orð[0:length])
                    print(stafur[-1])
                    sum += 1
            except:
                if sum == 0:
                    print(orð)