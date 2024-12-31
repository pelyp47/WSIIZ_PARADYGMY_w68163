def generateAndRunCode(template, placeholders):
    try:
        filledCode = template.format(**placeholders)
    except KeyError as e:
        raise ValueError(f"Brakuje wartości dla placeholdera: {e}")
    
    try:
        compiledCode = compile(filledCode, "<generated_code>", "exec")
    except SyntaxError as e:
        raise ValueError(f"Generowany kod zawiera błąd składni: {e}")
    
    globalNamespace = {}
    localNamespace = globalNamespace
    try:
        exec(compiledCode, globalNamespace, localNamespace)
    except Exception as e:
        raise RuntimeError(f"Błąd podczas wykonywania kodu: {e}")
    
    if "result" in localNamespace:
        return localNamespace["result"]
    return None

# Przykłady użycia
template1 = """
def generatedFunction(x):
    return x {operator} {value}

result = generatedFunction({input})
"""

placeholders1 = {
    "operator": "+",
    "value": "10",
    "input": "5"
}

template2 = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial({number})
"""

placeholders2 = {
    "number": "6"
}

try:
    result1 = generateAndRunCode(template1, placeholders1)
    print(result1)

    result2 = generateAndRunCode(template2, placeholders2)
    print(result2)

except (ValueError, RuntimeError) as e:
    print(e)
