def min_element(start_index, numbers):
    n = len(numbers)
    min_index = start_index
    for number in range(start_index, n):
        if numbers[number] < numbers[min_index]:
            min_index = number
    return min_index

def swap(i, j, items):
    temp = []
    temp = items[i]
    items[i] = items[j]
    items[j] = temp
a = [1, 2, 4,-8, 20]
swap(0,3, a)
print(a)

"""def selection_sort(numbers):

    for i in range(0, len(numbers)):
        min_ = min_element(i, numbers)
        swap(i, min_, numbers)

print(selection_sort(a))"""

def difference(items1, items2):
    result = []
    for a in items1:
        if a not in items2:
            result.append(a)
    return result
    # used is result of difference; difference result is not_used indexes
    
def selection_sort_not_destructive(numbers):
    b = []
    used = []
    # for index in range ... not in used:
    
    return b

