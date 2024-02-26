

zero = [[0] * 3] * 2
sorrow = zero[:]

zero[0][0] = 1
zero[0].pop()
zero[0].pop()

print(f"Original: {zero}")
print(f"Copy: {sorrow}")