import numpy

def searchMetaHeuristicSolution(initialSolution, penaltiesTablesDict):
    returnSolution = initialSolution.copy()

    maxClassData = None
    maxPenaltyIndexes = None
    
    maxClassData, maxPenaltyIndexes = __searchMaxPenalty(penaltiesTablesDict)
    print(str(maxClassData.semesterNumber) + maxClassData.shift)
    print(maxPenaltyIndexes)
    


def __searchMaxPenalty(penaltiesTablesDict):
    maxGlobalPenalty = 0
    # Para cada turma
    for classData, penaltyTable in penaltiesTablesDict.copy().items():
        penaltyTable = numpy.array(penaltyTable.copy())
        maxTableValue = numpy.amax(penaltyTable)
        if maxTableValue < maxGlobalPenalty:
            continue #maior penalidade da tabela não é o maximo de todas -> pula iteracao
        maxGlobalPenalty = maxTableValue
        maxClassData = classData
        maxPenaltyIndexes = numpy.unravel_index(penaltyTable.argmax(), penaltyTable.shape)
    return maxClassData, maxPenaltyIndexes
        