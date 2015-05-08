def is_increasing(seq):
    for index in range(0, len(seq) -1):
        if seq[index] > seq[index + 1]:
            return False
    return True


print(is_increasing([1,2,3,6,7]))

