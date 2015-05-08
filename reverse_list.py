def reverse_list(items):
    index = len(items) - 1
    reversed_list = []

    while index >= 0:
        reversed_list = reversed_list + [items[index]]
        index = index - 1

    return reversed_list

def reverse_list_for(items):
    reversed_list = []
    for item in items:
        reversed_list = [item] + reversed_list

    return reversed_list

