boxes=[1, 1, 3, 1, 1, 3]
maxWeight = 5

boxes.sort(reverse=True)

steps = []

for weight in boxes:
    added = False


    for step in steps:
        if sum(step) + weight <= maxWeight:
            step.append(weight)
            added = True
            break

    if not added:
        steps.append([weight])

print(len(steps))
print(steps)

#wyjaśninie: dodajemy największą liczbę i probujemy dodać coraz mniejsze jeżeli mieszczą się na jeden step, jest to najbardziej wydajne w tym przypadku, czym i jest algorytm zachlanny.