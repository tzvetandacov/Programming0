n = input("enter digit")
n = int(n)

# n = 20

start = 1 #2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,110
sum = 0   #2,6,12,20,30,42,56,72,90,110

while start <= n:
    if start % 2 == 0:
        sum = sum + start
        print(start)

    start = start + 1

print(sum)
