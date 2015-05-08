def tail(list):

    result = []

    for index in range(1, len(list)):
        item = list[index]
        result += [item]

    return result
print(tail([2,3,4,6,7]))

def tail_string(string):

    result = ""

    for index in range(1,len(string)):
        result += string[index]
    return result
print(tail_string("Darina"))