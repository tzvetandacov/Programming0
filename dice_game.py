from random import randint

n = int ( input ("Enter Dice side:") )
Player_1 = input ("Enter first player name:")
Player_2 = input ("Enter second player name:")

player_1_dice_roll = randint (1, n)

player_2_dice_roll = randint (1, n)

print ( Player_1 + " rolled: " + str (player_1_dice_roll))


if player_1_dice_roll == player_2_dice_roll:
    print ("Tie!")

elif player_1_dice_roll > player_2_dice_roll:
    print ("The Winner is: " + Player_1)
else:
    print (" The Winner is: " + Player_2)
