def is_increasing(items):

    for index in range(1, len(items)):
        if items[index] > items[index -1]:
            pass
        else:
            return False
    return True
print(is_increasing([1,2,3,4,5,6,7,8]))