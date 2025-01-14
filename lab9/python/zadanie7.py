from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x: x % 2 == 0, nums))
evenSum = reduce(lambda x, y: x + y, even)
print("Liczby parzyste:", even)
print("Suma parzystych:", evenSum)