def highest(items):
    current_high = 0 #3,5,6
    counter = 0 #1,2,3
    index = 0 #1,2
    for item in items:
        if items[index] > current_high:
            current_high = items[index]
            counter = counter + 1
            index = index + 1
        else:
            index += 1
    return counter
#items = [2, 3, 5, 6, 2, 6, 8]
print(highest([3, 5, 2, 1, 6, 10, 3, 4, 1, 29, 30, 80]))
