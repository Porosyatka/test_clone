def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:  # a < b
        return gcd(a, b-a)


print("a=7, b=3. Наибольший общий делитель равен ", gcd(7, 3))
print("a=54, b=24. Наибольший общий делитель равен ", gcd(54, 24))
print("a=4, b=11. Наибольший общий делитель равен ", gcd(4, 11))
print("a=1071, b=462. Наибольший общий делитель равен ", gcd(1071, 462))
