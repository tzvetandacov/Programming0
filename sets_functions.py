a = [1,2,3,4,13,5,4,3,2,1]
b = [1,2,3,4,5,6,7,8,9,16,24,5,3]
def setify(items):
# Da ne se povtarqt elementi v noviq spisyk
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
#print(setify(b))


def union(list1, list2):
    return setify(list1 + list2)
print(union(a, b))




def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    for item2 in list2:
        if item2 in list1:
            result.append(item2)
    result = setify(result)
    return result
#print(intersection(a, b))



def cartesian_product(list1, list2):
    result = []
    for item in setify(list1):
        for item2 in setify(list2):
            result += [(item, item2)]
    return result
#print(cartesian_product(a, b))
