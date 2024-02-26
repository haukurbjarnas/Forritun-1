my_input = (input(""))

splitter = my_input.split()

fjöldi, taskan = splitter



hinar_töskurnar = input("")
runa = (hinar_töskurnar.split(" "))

lengd = len(runa)

sum = 2

for i in range(lengd+2):
    new_sum = sum + 1
    if taskan == runa[0]:
        print("fyrst")
        break
    if taskan == runa[1]:
        print("naestfyrst")
        break
    if taskan == runa[sum]:
        print(f"{new_sum} fyrst")
        break
    sum += 1