def sends_of_time(dolars):
    dolar = "$"
    star = "*"
    multiple_star = 1
    reverse = False
# rows = number of dolars
    if dolars % 2 == 0:
        dolars += 1
    for row in range(0, dolars):
        print((multiple_star * star) + (dolar * dolars) + (multiple_star * star))
        if not reverse:
            dolars -= 2
            multiple_star += 1
        else:
            dolars += 2
            multiple_star -= 1
        if dolars == 1:
            reverse = True

print(sends_of_time(34))



