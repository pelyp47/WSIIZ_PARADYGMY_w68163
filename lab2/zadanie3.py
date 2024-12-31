def analyzeMixedData(data):
    numbers = filter(lambda x: isinstance(x, (int, float)), data)
    maxNumber = max(numbers, default=None)

    strings = filter(lambda x: isinstance(x, str), data)
    longestString = max(strings, key=len, default=None)
    
    tuples = filter(lambda x: isinstance(x, tuple), data)
    largestTuple = max(tuples, key=len, default=None)

    return {
        "maxNumber": maxNumber,
        "longestString": longestString,
        "largestTuple": largestTuple,
    }

# Przykład użycia
data = [
    42, 
    "hello", 
    (1, 2, 3), 
    3.14, 
    "world", 
    (4, 5, 6, 7), 
    {"key": "value"}, 
    "a very long string",
    [1, 2],
    None
]

result = analyzeMixedData(data)
print(result["maxNumber"])
print(result["longestString"])
print(result["largestTuple"])
