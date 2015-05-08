A = [2, 0, 10, -2, 5, 1, -5]
B = []
def min_element(numbers):
    min_index = 0
    index = 0
    for number in A:
        if number < A[min_index]:
            min_index = index
        index += 1
    return min_index
print(min_element(A))


def basic_sort(numbers):
    n = len(A)
    while A > []:
    #while len(B) != n:
        min = min_element(A)
        B.append(A[min])
        del A[min]
    return B
print(basic_sort(A))


