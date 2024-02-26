current_year = None

file = open("num.txt", "r")

for line in file:
    year_and_month, index_num = line.split()
    only_year = year_and_month[0:4]
    