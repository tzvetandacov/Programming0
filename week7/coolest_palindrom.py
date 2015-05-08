#from reverse_str import reverse_str
def reverse_str(string):
    res = ""
    for ch in string:
        res = ch + res
    return res

def is_palindrom(string):
    string = string.lower()
    result = ""
    for ch in string:
        if ch == "," or ch == "." or ch == "-" or ch == "!" or ch == "?" or ch== ":" or ch == ";" or ch == " ":
            pass
        else:
            result += ch

    if reverse_str(result) == result:
        return True
    else:
        return False
print(is_palindrom("A, Toyota"))

