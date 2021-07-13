'''Проверка отсортирован ли массив?
 параметр ascending: если True  - по возрастанию
 если False -  по убыванию
'''


def check_sorted(A, ascending=True):
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(A)-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    print(flag)
    return flag


A = [1, 3, 5, 82]
check_sorted(A)
