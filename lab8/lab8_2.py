
def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)


def generate_number(N: int, M: int, prefix=None):
    '''
            Генерирует все числа (с лидирующими незначащими нулями)
            в N-ричной системе счисления (N <= 10) длины М
    '''
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


# Только для двоичной Системы исчисления
gen_bin(2)
# Для произвольной системы иссчисления.
generate_number(2, 3)
