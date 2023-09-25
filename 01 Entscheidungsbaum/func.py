import numpy as np

def gini(input):
    decisions = input[1:, 3]
    decisionCount = {}
    for decision in decisions:
        if (decision not in decisionCount):
            decisionCount[decision] = 1
        else:
            decisionCount[decision] += 1

    print(decisionCount)

    decisionDivisions = []
    for decision in decisionCount:
        decisionDivisions.append(decisionCount[decision] / len(decisions))

    return 1 - np.sum(np.square(decisionDivisions))