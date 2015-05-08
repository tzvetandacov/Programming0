def count_item(item, list):

    count = 0
    for element in list:
        if item == element:
            count += 1

    return count

print(count_item(2, [2,5,6,7,2,5,6,2]))
