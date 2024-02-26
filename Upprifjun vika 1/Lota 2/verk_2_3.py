budget = int(input())
cloud = int(input())
equator = int(input())
elevator = int(input())

if budget > cloud+equator+elevator:
    print("Budget is sufficient.")
elif budget < cloud+equator+elevator:
    print("Budget is insufficient.")