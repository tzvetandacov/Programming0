def startswith(search, string):
    search = str(search)
    string = str(string)

    for index in range(0, len(search)):
        if search[index] != string[index]:
            return False 
        else: pass

    return True

def str_drop(n, string):
    result = ""
    for index in range(n, len(string)):
        result += string[index]
    return result
def reverse_str(string):
    result = ""
    for ch in string:
        result = ch + result
    return result
def trim_begin(string):
    
    while startswith(" ", string):
        string = str_drop(1, string)
    

    return string

def trim_end(string):
    return reverse_str(trim_begin(reverse_str(string)))


def trim(string):
    return trim_end(trim_begin(string))


def inner_trim(string):
    string = trim(string)
    result = ""
    for index in range(0, len(string)):
        
        if string[index] == " " and string[index +1] == " ":
            pass
        else:
            result += string[index]
    
    return result
print(inner_trim("  lele      tova     ako      sraboti               ebasi     "))
  

