score = input("Enter score: ")
score = int(score)
if 0 < score <= 50:
    print("Слаб 2")
elif 50 < score <=60:
    print("Среден 3")
elif 60 < score <= 70:
    print( "Добър 4")
elif 70 < score <= 80:
    print("Много добър 5")
elif 80 < score < 100:
    print("Отличен 6")
elif score == 100:
    print("Много отличен 7")
    
