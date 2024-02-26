def sum_of_range(start, end, step):
    sum = 0
    for i in range (start, end+1, step):
        sum += i
    return sum