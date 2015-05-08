matrix = [ [1, 1, 1, 0],
           [0, 0, 0, 0],
           [1, 1, 0, 0]]
def order_of_seats(cinema):
    result = []
    index_row = len(matrix)
    index_col = len(matrix[0])
    """for index in range(0, len(cinema)):
        result += [(sum(cinema[index]), index + 1 )]
    return sorted(result)
print(order_of_seats(cinema))"""
    while index_row >= 0:
        if sum(matrix[index_row]) == len(matrix)






