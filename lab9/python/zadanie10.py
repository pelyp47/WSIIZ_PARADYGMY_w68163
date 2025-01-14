def checkPalindrom(l):
    return l == list(reversed(l))

liczby = [1, 2, 3, 2, 0]
print("Czy lista jest palindromem?", checkPalindrom(liczby))