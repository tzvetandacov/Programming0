n = input("Please enter a digit: ")
n = int(n)

start = 1
numbers = []
while start <= n:
    number = input("Enter number: ")
    number = int(number)
    if number % 2 == 0:
        numbers += [number]
        
    start +=1
    print(numbers)
