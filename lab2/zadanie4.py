from functools import reduce

def validateMatrixDimensions(matrix1, matrix2, operation):
    if operation == "add":
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Macierze muszą mieć takie same wymiary do dodawania.")
    elif operation == "multiply":
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej.")

def addMatrices(matrix1, matrix2):
    validateMatrixDimensions(matrix1, matrix2, "add")
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

def multiplyMatrices(matrix1, matrix2):
    validateMatrixDimensions(matrix1, matrix2, "multiply")
    return [
        [sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
         for j in range(len(matrix2[0]))]
        for i in range(len(matrix1))
    ]

def applyCustomOperation(x, y, operation):
    return eval(operation)

def combineMatrices(matrices, operation, customOperation=None):
    if operation == "add":
        return reduce(addMatrices, matrices)
    elif operation == "multiply":
        return reduce(multiplyMatrices, matrices)
    elif operation == "custom":
        if not customOperation:
            raise ValueError("Musisz podać niestandardową operację dla 'custom'.")
        return reduce(lambda x, y: applyCustomOperation(x, y, customOperation), matrices)
    else:
        raise ValueError(f"Nieznana operacja: {operation}")

# Przykład użycia
matricesToAdd = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

matricesToMultiply = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[2, 0], [1, 2]]
]

customOperation = "[[x[i][j] + 2 * y[i][j] for j in range(len(x[0]))] for i in range(len(x))]"

try:
    resultAdd = combineMatrices(matricesToAdd, "add")
    print(resultAdd)
    
    resultMultiply = combineMatrices(matricesToMultiply, "multiply")
    print(resultMultiply)

    resultCustom = combineMatrices(matricesToAdd, "custom", customOperation)
    print(resultCustom)

except ValueError as e:
    print("Błąd:", e)
