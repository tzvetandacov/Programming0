def drop(n, list):
    result = []
    index = 0
    if n >= len(list):
        print("Not possible!")

    while index < len(list) -n:
        result += [list[index + n]]
        index += 1


    return result
print(drop(10, [2,3]))