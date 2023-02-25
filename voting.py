# 201649047 Boyang Ji

import numpy as np


def generatePreferences(values):
    """
    The input values to this function is a worksheet
    corresponding to an xlsx file.
    The output of this function is a dictionary
    """
    max_row = values.max_row
    max_column = values.max_column
    # Add empty list based on maximum number of rows
    array = [[] for _ in range(len(max_row))]
    for i in range(1, max_row+1):
        for j in range(1, max_column+1):
            cell_obj = values.cell(row=i, column=j)
            array[i - 1].append(cell_obj.value)
    listSet = []
    for list in array:
        index = []
        for i in range(len(list)):
            index.append(i + 1)
        dic = {key: val for key, val in zip(index, list)}
        sortedResult = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)
        # Store the alternatives' number and score in a dictionary and
        # sort the dictionary by score and number
        sortedIndex = []
        for i in range(len(sortedResult)):
            sortedIndex.append(sortedResult[i][0])
        listSet.append(sortedIndex)
    agent = []
    for i in range(len(array)):
        agent.append(i + 1)
    resultDict = {key: val for key, val in zip(agent, listSet)}
    return resultDict


def tieBreaking(value, candidateWinner, preferences):
    """
    The value parameter contains max, min or the number of the agent
    max: select the one with the highest number
    min: select the one with the lowest number
    agent i: select the one that agent ranks the highest in preference ordering
    """
    try:
        if value == "max":
            return max(candidateWinner)
        elif value == "min":
            return min(candidateWinner)
        elif value in range(1, len(preferences) + 1):
            for i in preferences[value]:
                if i in candidateWinner:
                    return i
        else:
            raise IndexError
    except IndexError:
        print("Agent does not exist")


def dictatorship(preferenceProfile, agent):
    """
    Input a preference profile represented by a dictionary
    and an integer corresponding to an agent
    Output the winner that ranks first in each agent according to each agent
    """
    try:
        if agent in range(1, len(preferenceProfile) + 1):
            choice = preferenceProfile[agent]
            return choice[0]
        else:
            raise IndexError
    except IndexError:
        print("Agent does not exist")


def scoringRule(preferences, scoreVector, tieBreak):
    """
    A preference profile represented by a dictionary
    A score vector is a vector of lengths equal to the number of alternatives
    The tiebreak is one of the arguments to the tebreaking function
    This function returns the alternative with the highest total score
    """
    scoreVector = sorted(list(scoreVector), reverse=True)
    # Sort the scoreVector
    try:
        if len(scoreVector) == len(preferences[1]):
            list1 = []
            for i in preferences.values():
                list1.append(i)
            scoreSum = {}
            for i in list1:
                for j in range(len(i)):
                    if i[j] not in scoreSum:
                        scoreSum[i[j]] = scoreVector[j]
                    else:
                        scoreSum[i[j]] += scoreVector[j]
            candidateWinner = []
            for i in scoreSum.keys():
                if scoreSum[i] == max(scoreSum.values()):
                    candidateWinner.append(i)
            if len(candidateWinner) == 1:
                return candidateWinner[0]
            else:
                return tieBreaking(tieBreak, candidateWinner, preferences)
        else:
            raise IndexError
    except IndexError:
        print("Incorrect input")
        return False


def plurality(preferences, tieBreak):
    """
    The winner is the alternative that appears the most times
    in the first position of the agents' preference orderings.
    """
    firstSum = {}
    for value in preferences.values():
        if value[0] not in firstSum:
            firstSum[value[0]] = 1
        else:
            firstSum[value[0]] += 1
    candidateWinner = []
    for i in firstSum.keys():
        if firstSum[i] == max(firstSum.values()):
            candidateWinner.append(i)
    if len(candidateWinner) == 1:
        return candidateWinner[0]
    else:
        return tieBreaking(tieBreak, candidateWinner, preferences)


def veto(preferences, tieBreak):
    """
    Every agent assigns 0 points to the alternative that they rank in the last position
    and 1 point to every other alternative.
    The winner is the alternative with the most number of points.
    """
    list1 = []
    for i in preferences.values():
        list1.append(i)
    scoreSum = {}
    for i in list1:
        for j in range(len(i)):
            if i[j] not in scoreSum and j != len(i) - 1:
                scoreSum[i[j]] = 1
            elif  i[j] in scoreSum and j != len(i) - 1:
                scoreSum[i[j]] += 1
    candidateWinner = []
    for i in scoreSum.keys():
        if scoreSum[i] == max(scoreSum.values()):
            candidateWinner.append(i)
    if len(candidateWinner) == 1:
        return candidateWinner[0]
    else:
        return tieBreaking(tieBreak, candidateWinner, preferences)


def borda(preferences, tieBreak):
    """
    the alternative ranked at position j receives a score of m-j
    m is the number of alternatives
    The winner is the alternative with the highest score
    """
    list1 = []
    for i in preferences.values():
        list1.append(i)
    scoreSum = {}
    for i in list1:
        for j in range(len(i)):
            if i[j] not in scoreSum:
                scoreSum[i[j]] = len(i) - j - 1
            else:
                scoreSum[i[j]] += len(i) - j - 1
    candidateWinner = []
    for i in scoreSum.keys():
        if scoreSum[i] == max(scoreSum.values()):
            candidateWinner.append(i)
    if len(candidateWinner) == 1:
        return candidateWinner[0]
    else:
        return tieBreaking(tieBreak, candidateWinner, preferences)


def harmonic(preferences, tieBreak):
    """
    The alternative ranked at position j receives a score of 1/j
    The winner is the alternative with the highest score
    """
    list1 = []
    for i in preferences.values():
        list1.append(i)
    scoreSum = {}
    for i in list1:
        for j in range(len(i)):
            if i[j] not in scoreSum:
                scoreSum[i[j]] = 1 / (j + 1)
            else:
                scoreSum[i[j]] += 1 / (j + 1)
    candidateWinner = []
    for i in scoreSum.keys():
        if scoreSum[i] == max(scoreSum.values()):
            candidateWinner.append(i)
    if len(candidateWinner) == 1:
        return candidateWinner[0]
    else:
        return tieBreaking(tieBreak, candidateWinner, preferences)


def STVAuxiliaryFun(dict):
    """
    This is a auxiliary function
    that completes the iterative process of the main function
    When the maximum value equals the minimum value, end the iteration
    """
    alternatives = list(dict.keys())
    maxValue = max(dict.values())
    minValue = min(dict.values())
    if maxValue != minValue:
        for i in alternatives:
            if dict[i] == minValue:
                del dict[i]
                alternatives.remove(i)
        return STVAuxiliaryFun(dict)
    else:
        return dict


def STV(preferences, tieBreak):
    """
    This process is repeated, the alternatives that appear the least frequently
    in the first position of agents' rankings are removed,
    and this last set is the set of possible winners
    This iterative process is completed by the auxiliary function
    """
    dict = {}
    for i in range(1, len(preferences[1]) + 1):
        dict[i] = 0
    list1 = []
    for i in preferences.values():
        list1.append(i[0])
    for i in list1:
        if i in dict:
            dict[i] += 1
    firstSum = STVAuxiliaryFun(dict)
    candidateWinner = []
    for i in firstSum.keys():
        if firstSum[i] == max(firstSum.values()):
            candidateWinner.append(i)
    if len(candidateWinner) == 1:
        return candidateWinner[0]
    else:
        return tieBreaking(tieBreak, candidateWinner, preferences)


def rangeVoting(values, tieBreak):
    """
    The input values is a worksheet corresponding to an xlsx file
    The winner is the alternative that has the maximum sum of numerical values in the xlsx file
    """
    preferences = generatePreferences(values)
    max_row = values.max_row
    max_column = values.max_column
    array = []
    while len(array) != max_row:
        array.append([])
    for i in range(1, max_row+1):
        for j in range(1, max_column+1):
            cell_obj = values.cell(row=i, column=j)
            array[i - 1].append(cell_obj.value)
    values = np.array(array)
    valuesSum = values.sum(axis=0).tolist()
    index = []
    for i in range(1, len(values[0]) + 1):
        index.append(i)
    scoreSum = {key: val for key, val in zip(index, valuesSum)}
    candidateWinner = []
    for i in scoreSum.keys():
        if scoreSum[i] == max(scoreSum.values()):
            candidateWinner.append(i)
    if len(candidateWinner) == 1:
        return candidateWinner[0]
    else:
        return tieBreaking(tieBreak, candidateWinner, preferences)
