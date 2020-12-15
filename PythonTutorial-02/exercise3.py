
def ListToDecimal(L):
    result = 0
    L_len = len(L)
    for i in range(L_len):
        result += L[i] * 10 ** (L_len - i - 1)

    return result

def AddTwoLists(L1, L2):
    N1 = ListToDecimal(L1)
    N2 = ListToDecimal(L2)
    return N1 + N2

L1 = [5, 2, 3]
L2 = [1, 0, 2, 4]

print(AddTwoLists(L1, L2))