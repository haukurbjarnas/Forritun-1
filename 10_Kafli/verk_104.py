shiritori = input("")


new_shiritori = input("")

correct = []

incorrect = []

correct.append(shiritori.lower())

sum = 0


while new_shiritori != "x":
    endir = correct[sum]
    lower_new = new_shiritori.lower()
    if lower_new[0] == endir[-1]:
        correct.append(new_shiritori.lower())
        sum += 1
    else:
        incorrect.append(new_shiritori.lower())
    new_shiritori = input("")



for i in correct:
    print(i, end=" ")

if len(correct) == 0:
    print("\n")

if len(correct) > 0 and len(incorrect) > 0:
    print("")

for j in incorrect:
    print(j, end=" ")

if len(incorrect) == 0:
    print("\n")
