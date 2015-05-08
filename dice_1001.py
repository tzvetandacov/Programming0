from random import randint

Ivan_result = 1001
Maria_result = 1001
#if Ivan_result == 0:
#    print("Ivan is the real Winner!")
#elif Maria_result ==0:
#    print("Maria is the real Winner!")
#elif  Ivan_result != 0 and Maria_result != 0:

while Maria_result != 0 or Ivan_result !=0:
    Ivan_dice_1 = randint(1, 6)
    print("Ivan dice 1:",Ivan_dice_1)
    Ivan_dice_2 = randint(1, 6)
    print("Ivan dice 2:",Ivan_dice_2)
    Ivan_dice_3 = randint(1, 6)
    print("Ivan dice 3:",Ivan_dice_3)
    Ivan_dice_4 = randint(1, 6)
    print("Ivan dice 4:",Ivan_dice_4)
    Ivan_dice_5 = randint(1, 6)
    print("Ivan dice 5:",Ivan_dice_5)
    print("Ivan's current result is:", Ivan_result)
    if Ivan_result > 0:
        Ivan_result = Ivan_result - Ivan_dice_1 - Ivan_dice_2 - Ivan_dice_3 - Ivan_dice_4 - Ivan_dice_5
    elif Ivan_result < 0:
        Ivan_result = Ivan_result + Ivan_dice_1 + Ivan_dice_2 + Ivan_dice_3 + Ivan_dice_4 + Ivan_dice_5
    elif Ivan_result == 0:
        print("Ivan is the final Winner!")

    Maria_dice_1 = randint(1, 6)
    print("Maria dice 1:",Maria_dice_1)
    Maria_dice_2 = randint(1, 6)
    print("Maria dice 2:",Maria_dice_2)
    Maria_dice_3 = randint(1, 6)
    print("Maria dice 3:",Maria_dice_3)
    Maria_dice_4 = randint(1, 6)
    print("Maria dice 4:",Maria_dice_4)
    Maria_dice_5 = randint(1, 6)
    print("Maria dice 5:",Maria_dice_5)
    print("Maria's current result is: ", Maria_result)
    if Maria_result > 0:
        Maria_result = Maria_result - Maria_dice_1 - Maria_dice_2 - Maria_dice_3 - Maria_dice_4 - Maria_dice_5
    elif Maria_result < 0:
        Maria_result = Maria_result + Maria_dice_1 + Maria_dice_2 + Maria_dice_3 + Maria_dice_4 + Maria_dice_5

    if Maria_result == 0:
        print("Maria is the final Winner")

    
