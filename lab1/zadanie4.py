def knapsackProcedural(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1][0] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    selectedItems = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selectedItems.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selectedItems

def knapsackFunctional(items, capacity):
    def knapsackRecursive(i, w):
        if i == 0 or w == 0:
            return 0, []
        if items[i - 1][0] > w:
            return knapsackRecursive(i - 1, w)
        else:
            withoutItem, withoutList = knapsackRecursive(i - 1, w)
            withItem, withList = knapsackRecursive(i - 1, w - items[i - 1][0])
            withItem += items[i - 1][1]

            if withItem > withoutItem:
                return withItem, withList + [items[i - 1]]
            else:
                return withoutItem, withoutList

    return knapsackRecursive(len(items), capacity)

# [... (waga, wartość)]
items = [(1, 3), (2, 10), (4, 5), (5, 6)]
capacity = 5

# Proceduralne podejście
maxValueProcedural, selectedItemsProcedural = knapsackProcedural(items, capacity)
print(maxValueProcedural)
print(selectedItemsProcedural)

# Funkcyjne podejście
maxValueFunctional, selectedItemsFunctional = knapsackFunctional(items, capacity)
print(maxValueFunctional)
print(selectedItemsFunctional)