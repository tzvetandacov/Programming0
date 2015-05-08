"""def count_words(items): # [ gosho, pesho, mitko...]
    
     value = 1
     dictionary = {}
     
    for item in items:
        item = value
        dictionary = dictionary[key] + [item]
        
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
       
   return dictionary
a = [pesho, gosho, pesho]
print(a)"""

def count_words2(words):
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result
