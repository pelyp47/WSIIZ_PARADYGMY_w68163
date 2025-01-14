def permutation(list, way=[]):
    if not list:
        print(way)
    for i in range(len(list)):
        permutation(list[:i] + list[i+1:], way + [list[i]])

liczby = [1, 2, 3]
permutation(liczby)