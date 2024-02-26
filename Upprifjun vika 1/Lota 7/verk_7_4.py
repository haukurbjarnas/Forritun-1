def sum_of_range(start, end, step):

    sum = 0

    for num in range(start, end+1, step):
        sum += num

    return sum

print(sum_of_range(5, 10, 7))