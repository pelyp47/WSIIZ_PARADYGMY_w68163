def Calculator():
    print("Choose option:")
    print("1. Adding")
    print("2. Minus")
    print("3. Multiply")
    print("4. Devide")
    
    choice = input("Chose (1/2/3/4): ")
    a = float(input("Give first number: "))
    b = float(input("Give second number: "))

    if choice == '1':
        print("result:", a + b)
    elif choice == '2':
        print("result:", a - b)
    elif choice == '3':
        print("result:", a * b)
    elif choice == '4':
        if b != 0:
            print("result:", a / b)
        else:
            print("Error: didviding by 0")
    else:
        print("Choice mistake")

Calculator()