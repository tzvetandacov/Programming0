def index_in(index, items):
    return index >= 0 and index < len(items)
def hash_them(keys, values):
    
    dictionary = {}
    index = 0

    for key in keys:
        if index_in(index, values): # if True: index >= 0 and index < len(items)
            dictionary[key] = values[index] # result[key] ???
        else: # if NOT index >= 0 and index < len(items)
            dictionary[key] = None
        
         

        index += 1
         
    return dictionary
keys = ["Mitko", "Pesho", "Goshko", "Roger"]
values = [24, 45, 21]
a = hash_them(["name"], ["Ivan", 23])
print(a)
                         
