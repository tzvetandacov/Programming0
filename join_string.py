def join(delimiter, items):

    result = ""


    for item in items:
        if item == items[len(items) -1]:
            result += item
        else:
            result += item + delimiter


    return result

print(join("\n",["Rado", "obicha", "da", "kara", "snowboard", "1" , "2"]))
print(join("_",["Rado", "obicha", "da", "kara", "snowboard", "1" , "2"]))