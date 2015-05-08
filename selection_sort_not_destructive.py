a = [-90,30,-12,-166,15,23,24,12,13,14,-14,-13]

def min_element(numbers):
    min_index = 0
    for index in range(0, len(numbers)):
        if numbers[index] < numbers[min_index]:
            min_index = index
    return min_index

"""def min_element(numbers):
    min_index = 0
    index = 0
    while index < len(numbers):
        if numbers[index] < numbers[min_index]:
            min_index = index
        index += 1
    return min_index"""

def difference(original_list, used):
    result = []
    for item in original_list:
        if item not in used:
            result.append(item)
    return result
#print(difference([0,1,2,3,4,5,6,7,8], [4,3,6]))
def numbers_to_num_indexes(numbers):
    index = 0
    result = []
    while len(result) != len(numbers):
        result.append(index)
        index += 1
    return result
#print(numbers_to_num_indexes(a))




"""def not_destructive_sort(numbers):
    orig_list_index = numbers_to_num_indexes(numbers)
    result = []
    used_i = []
    while len(used_i) != len(numbers):
        #result.append(numbers[min_element(difference(numbers, used_i))])
        #used_i.append(min_element(difference(numbers, used_i)))
        result += [numbers[min_element(difference(orig_list_index, used_i))]]
        used_i += [min_element(difference(orig_list_index, used_i))]
    return result
print(not_destructive_sort(a))
print(a)"""
"""def unused numbers(numbers):
    result = []
    for index in difference(original_list, used):
        result.append(numbers[index])
    return result"""


def not_destructive_sort(numbers):
    result = []
    numbers_indexes = numbers_to_num_indexes(numbers)
    used_i = []
    while len(result) != len(numbers_indexes):
        unused_indexes = difference(numbers_indexes, used_i)
        print(unused_indexes)
        unused_numbers = []

        for index in unused_indexes:
            unused_numbers += [numbers[index]]
        #print(unused_numbers)
        result += [unused_numbers[min_element(unused_numbers)]]
        used_i += [min_element(numbers)] 

    
    return result

print(not_destructive_sort(a))
#print(a)

# Da opravq difference funkciqta da ne maha vsichki ednakvi elementi v rezultata