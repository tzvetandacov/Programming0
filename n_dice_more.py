n = input("Enter n: ")
n = int(n)


from random import randint
dice1 = randint(1, n)
print(dice1)

dice2 = randint(1, n)
print(dice2)

dice3 = randint(1, n)
print(dice3)
total_sum = dice1 + dice2 + dice3
print(total_sum)
