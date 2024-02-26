mb_per_month = int(input())

months_on_plan = int(input())

sum = mb_per_month

for i in range(months_on_plan):
    single_month = int(input())
    sum += (mb_per_month - single_month)

print(sum)