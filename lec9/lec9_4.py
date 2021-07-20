'''
Реализация бинарного поиска в массиве
требования - массив отсортирован
мы должны получить индекс границы
считаем что массив отсортирована по возрастанию
'''


def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right
