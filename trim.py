from str_drop import str_drop
from startswith import startswith
from reverse_str import reverse_str

def trim_begin(string):
    
    while startswith(" ", string):
        string = str_drop(1, string)
    

    return string

def trim_end(string):
    return reverse_str(trim_begin(reverse_str(string)))


def trim(string):
    return trim_end(trim_begin(string))

print(trim("   baba   "))