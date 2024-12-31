def validateDimensions(operation, matrix1, matrix2=None):
    if operation == "add":
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Macierze muszą mieć takie same wymiary do dodawania.")
    elif operation == "multiply":
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej.")
    elif operation == "transpose":
        pass
    else:
        raise ValueError(f"Nieznana operacja: {operation}")

def addMatrices(matrix1, matrix2):
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

def multiplyMatrices(matrix1, matrix2):
    return [
        [sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
         for j in range(len(matrix2[0]))]
        for i in range(len(matrix1))
    ]

def transposeMatrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def executeOperation(operation, matrices):
    result = None
    if operation == "add":
        exec("validateDimensions('add', matrices[0], matrices[1])")
        result = addMatrices(matrices[0], matrices[1])
    elif operation == "multiply":
        exec("validateDimensions('multiply', matrices[0], matrices[1])")
        result = multiplyMatrices(matrices[0], matrices[1])
    elif operation == "transpose":
        result = [transposeMatrix(matrix) for matrix in matrices]
    else:
        raise ValueError(f"Nieznana operacja: {operation}")
    return result

def parseAndExecute(command):
    lines = command.split("\n")
    operation = lines[0].strip()
    
    matrices = []
    for line in lines[1:]:
        matrix = eval(line.strip())
        matrices.append(matrix)
    
    result = executeOperation(operation, matrices)
    return result

# Przykład użycia
commandAdd = """add
[[1, 2, 3], [4, 5, 6]]
[[7, 8, 9], [10, 11, 12]]"""

commandMultiply = """multiply
[[1, 2], [3, 4]]
[[5, 6], [7, 8]]"""

commandTranspose = """transpose
[[1, 2, 3], [4, 5, 6]]"""
try:
    resultAdd = parseAndExecute(commandAdd)
    print(resultAdd)
    
    
    resultMultiply = parseAndExecute(commandMultiply)
    print(resultMultiply)
    
    resultTranspose = parseAndExecute(commandTranspose)
    print(resultTranspose)

except ValueError as error:
    print("Błąd:", error)
