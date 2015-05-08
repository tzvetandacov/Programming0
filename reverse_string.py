def reverse_string(string):
    
    reverse = ""
    index = len(string) - 1
    while index >= 0:
        reverse += string[index]

        index -= 1

    return reverse

#print(reverse_string("azobi4amma4ibozaE"))