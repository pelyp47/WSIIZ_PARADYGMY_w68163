def activitySelectionProcedural(tasks):
    tasks.sort(key=lambda x: (x[1], -x[2]))

    selectedTasks1 = []
    lastEndTime1 = 0
    totalReward1 = 0

    for start, end, reward in tasks:
        if start >= lastEndTime1:
            selectedTasks1.append((start, end, reward))
            lastEndTime1 = end
            totalReward1 += reward
    
    tasks.sort(key=lambda x: (-x[2], x[1]))

    selectedTasks2 = []
    lastEndTime2 = 0
    totalReward2 = 0
    for start, end, reward in tasks:
        if start >= lastEndTime2:
            selectedTasks2.append((start, end, reward))
            lastEndTime2 = end
            totalReward2 += reward

    return (totalReward1, selectedTasks1) if totalReward2 < totalReward1 else (totalReward2, selectedTasks2)
from functools import reduce
def activitySelectionFunctional(tasks):

    tasks = [sorted(tasks, key=lambda x: (x[1], -x[2])), sorted(tasks, key=lambda x: (-x[2], x[1]))]

    def selectTasks( remainingTasks, selectedTasks=[]):
        if not remainingTasks:
            return selectedTasks
        currentTask = remainingTasks[0]
        if not selectedTasks or currentTask[0] >= selectedTasks[-1][1]:
            return selectTasks(remainingTasks[1:], selectedTasks + [currentTask])
        return selectTasks(remainingTasks[1:], selectedTasks)

    selectedTasks = list(map( selectTasks, tasks))
    totalRewards = list(map(lambda tasks: sum(task[2] for task in tasks), selectedTasks))
    totalReward = max(totalRewards)
    selectedTask = selectedTasks[totalRewards.index(totalReward)]

    return totalReward, selectedTask
#[...(start, end, weight)]
tasks1 = [(1, 3, 5), (3, 5, 2), (0, 6, 100), (5, 7, 3), (8, 9, 1), (5, 9, 6)]
tasks2 = [(1, 3, 50), (3, 5, 25), (0, 6, 100), (5, 7, 30), (8, 9, 10), (5, 9, 60)]

# Proceduralne podejście
maxRewardProcedural, selectedTasksProcedural = activitySelectionProcedural(tasks2)
print(maxRewardProcedural)
print(selectedTasksProcedural)

# Funkcyjne podejście
maxRewardFunctional, selectedTasksFunctional = activitySelectionFunctional(tasks2)
print(maxRewardFunctional)
print(selectedTasksFunctional)


#Wyjaśnienie: tu nie można zdecydować jakie na pewno priorytet będzie najwydajniejszym
#większa waga/mniejszy koniec
#mniejszy koniec/większa waga