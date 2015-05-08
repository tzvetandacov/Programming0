n = input("Enter n: ")
n = int(n)

start = 1
numbers = []
max_current = numbers[0]

while start <=n:
    number = input()
    number = int(number)

    numbers = numbers + [number]
    
    start += 1



for number in numbers:
    if number > max_current:
        max_current = number
    
print(max_current)
