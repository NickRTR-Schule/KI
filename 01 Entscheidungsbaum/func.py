import numpy as np

def giniGesamt(input):
    decisions = input[1:, 3]
    decisionCount = {}
    for decision in decisions:
        if (decision not in decisionCount):
            decisionCount[decision] = 1
        else:
            decisionCount[decision] += 1

    decisionDivisions = []
    for decision in decisionCount:
        decisionDivisions.append(decisionCount[decision] / len(decisions))

    return 1 - np.sum(np.square(decisionDivisions))

def specificGini(input, column, value):
    decisions = []
    for row in input:
        if (row[column] == value):
            decisions.append(row[3])

    decisionCount = {}
    for decision in decisions:
        if (decision not in decisionCount):
            decisionCount[decision] = 1
        else:
            decisionCount[decision] += 1

    decisionDivisions = []
    for decision in decisionCount:
        decisionDivisions.append(decisionCount[decision] / len(decisions))

    return [1 - np.sum(np.square(decisionDivisions)), len(decisions)/len(input)]

def weightedGini(ginis):
    value = 0
    for gini in ginis:
        value += gini[0] * gini[1]

    return value

def gini(input, column):
    input = input[1:]

    values = []
    for row in input:
        if (row[column] not in values):
            values.append(row[column])

    ginis = []
    for value in values:
        ginis.append(specificGini(input, column, value))

    result = weightedGini(ginis)

    print("Weighted Gini for Column", column, ":", round(result, 2))

    return result

def bestGini(input):
    ginis = []
    for i in range(0, len(input[0]) - 1):
        ginis.append(gini(input, i))

    best = ginis.index(min(ginis))

    return best, input[0][best]