def count_vowels_consonants(word):
    dictionary = {"vowels": 0,
              "consonants": 0}

    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

   
    
    for letter in word:
        if letter in vowels:
            dictionary["vowels"] +=1
    for letter in word:
        if letter in consonants:
            dictionary["consonants"] += 1
            
            


    return dictionary
word = "Hello World"
print(count_vowels_consonants(word))
