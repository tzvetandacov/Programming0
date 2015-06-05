def is_decreasing(items):
    for index in range(1, len(items)):
        if items[index] < items[index -1]:
            pass
        else:
            return False
    return True
print(is_decreasing([100, 50, 20, 2]))