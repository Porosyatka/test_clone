'''Кузнечик
прыгает только вперед
находится на 1 позиции
может прыгать либо на +1 позицию или на +2 позиции
СКОЛЬКО РАЗЛИЧНЫХ ТРАЕКТОРИЙ (СПОСОБОВ) ДОПРЫГАТЬ ДО
ПОЗИЦИИ n
'''
'''ДВА ПОСЛЕДНИХ ПРИМЕРА НЕ РАБОТАЮТ!!!'''


def traj_num(n):
    K = [0, 1] + [0]*n
    for i in range(2, n+1):
        K[i] = K[i-2] + K[i-1]
    return K[n]


a = traj_num(10)
print(a)
'''Запретим некоторые клетки для посещение
и добавим еще 1 вариант прыжка +3 '''

'''
def count_trajectories(n, allowed: list):
    K = [0, 1, int(allowed[2])] + [0]*(n-3)
    for i in range(3, n+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    return K[n]


b = count_trajectories(10, [3, 6, 8])
print(b)
'''

'''Минимальная стоимость достижения клетки n
price[i] - цена за посещение конкретной клетки i
C[i] - cost, минимальная стоимость достижения клетки i
два варианта прыжка +1 и +2
C[i]=price[i] + min(C[i-2, C[i-1]])
C[1] = price[1]
C[2] = price[1] + price[2]
'''


def count_min_cost(n, price: list):
    C = [None, price[1], (price[1] + price[2])] + [0] * (n-2)
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[n]


g = count_min_cost(10, [2, 3])
print(g)
