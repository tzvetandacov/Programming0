from reverse_string import reverse_string

def endswith(search, string):

    search = reverse_string(search)
    string = reverse_string(string)

    for index in range(0, len(search)):
        if search[index] != string[index]:
            return False
        else: pass
    return True
print(endswith("ria", "Maria"))