n = input("enter digit")
n = int(n)

# 20

start = 1 #2,3,4,5,6,7,8,9
sum = 0   #1,4,9,16,25

while start <= n:
    if start % 2 != 0:
        sum = sum + start
        print(start)

    start = start + 1

print(sum)
