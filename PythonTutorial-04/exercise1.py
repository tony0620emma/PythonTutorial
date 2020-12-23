
def intersect_lists(L1, L2):
    result = []
    for value in L1:
        try:
            index = L2.index(value)
        except ValueError:
            pass
        else:
            result.append(L2.pop(index))
    return result

L1 = [1, 2, 2, 2, 1]
L2 = [2, 2]
print(intersect_lists(L1, L2))
L1 = [4, 6, 7, 4, 7, 5, 9, 9]
L2 = [3, 4, 5, 6, 7]
print(intersect_lists(L1, L2))