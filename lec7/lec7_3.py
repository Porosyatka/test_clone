def f(n: int):
    assert n >= 0, "Факториал отрицательного числа не вычисляем"
    if n == 0:
        return 1
    return f(n-1) * n


print(f(5))
