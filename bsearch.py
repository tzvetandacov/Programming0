def bsearch(x, xs):
    left = 0
    right = len(xs) -1

    while left <= right:
        mid = (left + right) // 2
        if xs[mid] == x:
            return True
        elif x < xs[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
print(bsearch(4, [0,1,2,3,4,5,6,7,8,24, 46, 789, 1256]))