def pow(a, n):
    return 1 if n == 0 else pow(a, n-1) * a


print(pow(2, 4))
print(pow(3, 3))
print(pow(4, 4))
print(pow(5, 4))


# лучшее быстродействие:
def pow2(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow2(a * a,  n // 2)
    else:
        return pow2(a, n-1) * a


print(pow2(2, 4))
print(pow2(3, 3))
print(pow2(4, 4))
print(pow2(5, 4))
