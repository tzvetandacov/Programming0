def sum_rows(matrix):
    sum_row = []
    for row in matrix:
        sum_row += [sum(row)]
    return sum_row

print(sum_rows([[1,2,3,4,5],[5,3,2,4,5]]))

def sum_columns(matrix):
    index_row = 0
    index_col = 0
    sum_col = 0
    sum_col_list = []
    while index_col < len(matrix):
        while index_row < len(matrix):
            sum_col += matrix[index_row][index_col]
            index_row += 1
        sum_col_list += [sum_col]    
        index_col += 1
        

    return sum_col_list

print(sum_columns([[1,2,3,4,5],[5,3,2,4,5],[1,2,3,4,5],[3,2,5,6,7],[2,4,6,8,9]]))

