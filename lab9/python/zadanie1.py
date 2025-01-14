def SumNumber(number):
    return sum(int(num) for num in str(abs(number)))

number = int(input("Podaj liczbę: "))
print("Suma cyfr:", SumNumber(number))