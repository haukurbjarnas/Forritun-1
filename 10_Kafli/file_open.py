import statistics

file_name = input("")

file_list = []
num_list = []
sum = 0
numbers = len(num_list)

try:
    with open(file_name, "r") as file:
        for line in file:
            for i in line:
                if ord(i) >= 48 and ord(i) <= 57:
                    file_list.append(line.replace("\n", " "))
                    break
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}.")

for i in file_list:
    for j in i:
        if ord(j) >= 48 and ord(j) <= 57:
            number = float(i)
            num_list.append(number)
            break

for i in num_list:
    print(round(i, 4), end=" ")

print("")

for i in num_list:
    sum += i
    print(round(sum, 4), end=" ")

sorted_list = sorted(num_list)

print("")

for i in sorted_list:
    print(round(i, 4), end=" ")

if len(file_list) == 0:
    print("")
    exit()

median = statistics.median(sorted_list)

print("")

print(round(median, 4))