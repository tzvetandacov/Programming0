stars = input("enter number of stars:")
stars = int(stars)
#stars = 18
if stars % 2 == 0:
    stars += 1

#def sends_of_time(number_of_stars):

star = "*"
dot = "."
multiple_dot = 1
should_reverse = False
for row in range(0, stars):
    print((multiple_dot*dot)+(stars*star)+(multiple_dot*dot))
    if should_reverse:
        stars += 2
        multiple_dot -= 1
    else:
        stars -= 2
        multiple_dot += 1
    if stars == 1:
        should_reverse = True


