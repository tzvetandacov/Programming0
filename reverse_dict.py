my_dict = {'x':1, 'y':2, 'z':3}

def swap_key_value(dictionary):

    result = {}
    for key in dictionary:
        value = dictionary[key]
        print(value)
        result[value] = key
    return result
print(swap_key_value(my_dict))
