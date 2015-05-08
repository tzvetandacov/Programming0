matrix = [[23,6,19,2,15 ],
          [4,12,25,8,16 ],
          [10,18,1,14,22],
          [11,24,7,20,3 ],
          [17,5,13,21,9]]

def sum_row(index, matrix):
    return sum(matrix[index])
#print(sum_row(2,matrix))

def sum_column(index, matrix):
    result = 0
    for row in matrix:
        result += row[index]
    return result
#print(sum_column(1, matrix))

def main_diagonal(matrix):
    result = 0
    index = 0
    for row in matrix:
        result += matrix[index][index]
        index += 1
    return result
#print(main_diagonal(matrix)) WORKS

def second_diagonal(matrix):
    index = 0
    result = 0 
    index = 0
    n = len(matrix) -1
    for row in matrix:
        result += matrix[index][n]
        index += 1
        n -= 1
    return result
#print(second_diagonal(matrix)) WORKS

def magic_square(matrix):
    refferent_result = main_diagonal(matrix)
    index_row = 0

    while index_row < len(matrix):
        if sum(matrix[index_row]) != refferent_result:
            return False
        index_row += 1
    for index in range(0, len(matrix)):
        if sum_column(index, matrix) != refferent_result:
            return False

    if second_diagonal(matrix) != refferent_result:
        return False
    else:
        return True
print(magic_square(matrix))