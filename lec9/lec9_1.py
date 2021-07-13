"""сортировка слиянием. Слияние отсортированных масивов
"""


def merge(A: list, B: list):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    print(i, k, n)
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    print(C)
    return C


A = [2, 4, 6, 9]
B = [1, 3, 5, 8, 11, 15]

merge(A, B)
