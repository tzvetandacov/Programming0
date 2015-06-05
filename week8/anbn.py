def is_an_bn(word):
    #a = 0
    #b = 0
    indexa = 0
    indexb = len(word) / 2
    if len(word) % 2 != 0:
        return False

    while indexa < (len(word) / 2):
        if word[indexa] != "a":
            return False
        elif word[indexa] == "a":
            #a += 1
            indexa += 1
    while indexb < len(word):

        if word[(indexb + len(word)) // 2] != "b":
            return False
        elif word[(indexb + len(word)) // 2] == "b":
            #b += 1
            indexb += 1
    #if a != b:
    #    return False
    #elif a == b:
    return True
print(is_an_bn("a" * 100000000 + "b" * 100000001))