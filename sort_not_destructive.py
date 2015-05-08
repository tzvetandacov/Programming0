def min_element(numbers):
    min_index = 0
    index = 0
    for number in numbers:
        if number < numbers[min_index]:
            min_index = index
        index += 1
    return numbers[min_index]

def difference(original_list, used):
    result = []
    for a in original_list:
        if a not in used:
            result.append(a)
    return result

def not_destructive_sort(numbers):
    result = []
    used = []
    while len(result) != len(numbers):
        result += [min_element(difference(numbers, used))]
        used += [min_element(difference(numbers, used))]
    return result
a = [90, 30, -12, -16, -98, 4]
print(not_destructive_sort(a))
print(a)
