players = int(input())
while players < 2:
    players = int(input())

sum = 0

for i in range(players):
    contribution = int(input())
    sum += contribution

print(f"The sum of all contributions is {sum}")
print(f"When {sum} is devided by {players} the remainder is {sum%players}")
print(f"The winner is {sum%players}")