def on_budget(books, budget):
    books = [0, 10, 100, 5, 3, 8, 25]
    budget = 35
    
    result = {"books on budget": 0, 
    "loan": 0}
    
    books = sorted(books)

    while budget !=0:
        for book in books:
            if budget - book > 0:
                result[0] += 1
        print(result)
    
    
