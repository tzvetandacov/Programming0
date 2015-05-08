def startswith(search, string):
    search = str(search)
    string = str(string)

    for index in range(0, len(search)):
        if search[index] != string[index]:
            return False 
        else: pass

    return True