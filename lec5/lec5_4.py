def resheto(N):
	""" Решето Эратосфена. Находим простые
	и составные числа - индексы массива
	"""
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    print(A)
    for k in range(N):
        print(k, "-", "простое" if A[k] else "составное")


c = int(input("Введите количество чисел в массиве: "))

resheto(c)
