player1 = input("enter player1 name:")
player2 = input("enter player2 name:")
from random import randint
player1_dice = randint(1, 6)
print(player1, "rolls", player1_dice)
player2_dice = randint(1, 6)
print(player2, "rolls", player2_dice)

if player1_dice > player2_dice:
    print(player1, "Wins!")
elif player1_dice == player2_dice:
    print("Toe")
else:
    print(player2, "Wins!")
