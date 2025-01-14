def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("n: "))
print(f"{n}-th Fibonacci:", fibonacci(n))