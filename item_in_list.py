def member(x, xs):
    found = False
    for memb in xs:
        if x == memb:
            found = True
            break
    
    return found
    
