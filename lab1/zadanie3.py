def optimizeTasksProcedural(tasks):
    tasks.sort(key=lambda x: (-x[1], x[0]))

    totalWaitingTime = 0
    currentTime = 0

    for time, _ in tasks:
        currentTime += time
        totalWaitingTime += currentTime

    return tasks, totalWaitingTime

from functools import reduce

def optimizeTasksFunctional(tasks):
    sortedTasks = sorted(tasks, key=lambda x: (-x[1], x[0]))
    totalWaitingTime = reduce(
        lambda acc, task: (acc[0] + task[0], acc[1] + acc[0] + task[0]),
        sortedTasks,
        (0, 0)
    )[1]

    return sortedTasks, totalWaitingTime
#[...(czas, waga)]
tasks = [(3, 50), (1, 20), (2, 30), (1, 60)]

# Proceduralne podejście
optimalTasksProcedural, waitingTimeProcedural = optimizeTasksProcedural(tasks.copy())
print(optimalTasksProcedural)
print(waitingTimeProcedural)

# Funkcyjne podejście
optimalTasksFunctional, waitingTimeFunctional = optimizeTasksFunctional(tasks.copy())
print( optimalTasksFunctional)
print( waitingTimeFunctional)

#wyjaśnienie: głównym jest posortować rosnącą po czasu i malejącą po wagach(czas większy priorytet)