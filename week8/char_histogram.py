def char_histogram(string):
    dictionary = {}
    for ch in string:
        if ch in dictionary:
            dictionary[ch] += 1
        else:
            dictionary[ch] = 1

    return dictionary
print(char_histogram("Aniesuperiemnogoumna"))