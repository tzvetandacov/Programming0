def is_an_bn(word):
    if word == "":
        return True
    if len(word) % 2 != 0:
        return False
    for index in range(0, (len(word) / 2)):
        if word[index] != "a":
            return False
    for index in range(len(word) / 2, len(word)):
        if word[index] != "b":
            return False
    return True
print(is_an_bn("aaaaaaaaaaaabbbbbbbbbbbb"))