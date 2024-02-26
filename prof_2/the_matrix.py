the_num = int(input(""))

matrix1_row1 = []
matrix1_row2 = []
matrix2_row1 = []
matrix2_row2 = []

matrix1_row1.append(the_num)

sum = 1

while sum < 3:
    the_num = int(input(""))
    matrix1_row1.append(the_num)
    sum+=1

while sum < 6:
    the_num = int(input(""))
    matrix1_row2.append(the_num)
    sum+=1

while sum < 9:
    the_num = int(input(""))
    matrix2_row1.append(the_num)
    sum+=1

while sum < 12:
    the_num = int(input(""))
    matrix2_row2.append(the_num)
    sum+=1

matrix1 = []
matrix2 = []
matrix1.append(matrix1_row1)
matrix1.append(matrix1_row2)
matrix2.append(matrix2_row1)
matrix2.append(matrix2_row2)

row_1_1 = matrix1_row1[0] + matrix2_row1[0]
row_1_2 = matrix1_row1[1] + matrix2_row1[1]
row_1_3 = matrix1_row1[2] + matrix2_row1[2]

matrix3_row1 = []
matrix3_row1.append(row_1_1)
matrix3_row1.append(row_1_2)
matrix3_row1.append(row_1_3)

row_2_1 = matrix1_row2[0] + matrix2_row2[0]
row_2_2 = matrix1_row2[1] + matrix2_row2[1]
row_2_3 = matrix1_row2[2] + matrix2_row2[2]

matrix3_row2 = []
matrix3_row2.append(row_2_1)
matrix3_row2.append(row_2_2)
matrix3_row2.append(row_2_3)

matrix3 = []
matrix3.append(matrix3_row1)
matrix3.append(matrix3_row2)

print(matrix1)
print(matrix2)
print(matrix3)
