string = input("enter string: ")

# ch stands for character

for ch in string:
    print(ch)


counter =0
vowels = "aeiouyAEIOUY"
for ch in vowels:
    if ch in string:
        counter +=1
        print(ch)

print(counter)
