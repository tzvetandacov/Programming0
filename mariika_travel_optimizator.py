def travels_opt(items):
    travels_list = []
    index = 0
    total_sum = 0
    for item in items:
        if item > 23:
            travels_list += [23]
        elif item < 23:
            travels_list += [item]
    for travel in travels_list:
        total_sum += travels_list[index]
        index += 1
        if total_sum > 50:
            total_sum = 50
            return 50
    return travels_list

print(travels_opt([24, 15, 24]))
            
