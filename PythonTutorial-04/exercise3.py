from sys import maxsize

def sum_of_sub_list(L, start, end):
    sum = 0
    for value in L[start:end]:
        sum += value
    return sum

def largest_sub_list(L):
    max = -maxsize
    max_sub_list = L
    for end in range(len(L) + 1):
        for start in range(end):
            sum = sum_of_sub_list(L, start, end)
            if sum > max:
                max = sum
                max_sub_list = L[start:end]
    return max_sub_list

L1 = [-2, 3, 4, -1, 0]
L2 = [1, 2, 3, 4, 5, -6, -7]
print(L1, " ->", largest_sub_list(L1))
print(L2, " ->", largest_sub_list(L2))

