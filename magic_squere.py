def sum_rows(matrix):
    
   
    last_index_row = matrix [len(matrix) -1]  #correct
    last_index_element = matrix[last_index_row][len(matrix[0]) -1] # correct
    last_index_column = last_index_element
    sum_rows_list = []
    list_of_numbers = []
    while last_index_column >= 0:
        
        while last_index_element >= 0:
            number = matrix[last_index_row][last_index_column]
            list_of_numbers += [number]

            
            last_index_element -= 1
                      
        sum_rows_list += [sum([row_numbers_list])]
        last_index_column -= 1
        
    return sum_rows_list

matrix =[[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]
print(sum_rows(matrix))

'''def sum_columns(matrix):

    last_index_element = ( len(matrix) -1)
    last_index_column = ( len(matrix) -1) # n - last element in row                     # 
    numbers_columns_list = []
    sum_columns = []
    
    while last_index_element >= 0:

        while last_index_column >= 0:

            number = matrix[last_index_column][last_index_element]
            numbers_columns_list += [number]
            

            last_index_column -= 1

        sum_columns = sum_columns + [sum(numbers_columns_list)]
        last_index_element -= 1
        

    return sum_columns
print(sum_columns(matrix))    
