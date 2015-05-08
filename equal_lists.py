def equal_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    for index in range(0, len(list1)):
        if list1[index] != list2[index]:
            return False
    return True

print(equal_lists([2,3,4],[2,3,4]))

