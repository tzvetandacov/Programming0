def count_zero_neighbours(items):
    
    """items = [1, -1, 2, -2, 5, -6, 6]"""

    index = 0

    result = []

    while index < len(items) - 1:

        if items[index] + items[index +1] == 0:
            result = result + [items[index]] 

            result = result + [items[index +1]]
            
        index += 1
            
    return result

items = [1, -1, 2, -2, 5, -6, 6]

print(count_zero_neighbours(items))
