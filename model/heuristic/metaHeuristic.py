import numpy

def searchMetaHeuristicSolution(initialSolution, penaltiesTablesDict):
    returnSolution = initialSolution.copy()

    maxGlobalPenalty = 0
    maxClassData = None
    maxPenaltyIndexes = None
    for classData, penaltyTable in penaltiesTablesDict.copy().items():
        penaltyTable = numpy.array(penaltyTable.copy())
        maxTableValue = numpy.amax(penaltyTable)
        if maxTableValue < maxGlobalPenalty:
            continue #maior penalidade da tabela não é o maximo de todas -> pula iteracao
        maxGlobalPenalty = maxTableValue
        maxClassData = classData
        maxPenaltyIndexes = numpy.unravel_index(penaltyTable.argmax(), penaltyTable.shape)

    print(str(maxClassData.semesterNumber) + maxClassData.shift)
    print(maxPenaltyIndexes)
        