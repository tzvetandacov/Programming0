def leet(string):
    string = string.lower()
    result = ""
    normal = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"," "]
    leet = ["(,)","\^/","3","|2","7","'/","|_|","!","()","|D","4","$","|)","|=","9","|-|","_|","|{","1","2","}{","(","\/","|3","|\|","|\/|","   "]
    for ch in string:
        for index in range(0, len(normal)):
            if ch == normal[index]:
                result += leet[index]
            """elif ch != normal[index]:
                result += ch """
    return result
print(leet("Az obicham mama"))
