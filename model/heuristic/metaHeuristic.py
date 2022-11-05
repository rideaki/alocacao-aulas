import copy
import numpy

def searchMetaHeuristicSolution(initialSolutionArg, penaltiesTablesDict):

    maxClassData = None
    maxPenaltyIndexes = None
    
    maxClassData, maxPenaltyIndexes = __searchMaxPenalty(penaltiesTablesDict)
    print(str(maxClassData.periodNumber) + maxClassData.shift)
    print(maxPenaltyIndexes)
    
    #Gerando permutações da timeTable[maxClassData] com indices maxPenaltyIndexes
    neighborSolutions = []
    timeTableWithMaxPenalty = copy.deepcopy(initialSolutionArg[maxClassData])
    maxBlockValue = timeTableWithMaxPenalty[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]]
    for i in range(len(timeTableWithMaxPenalty)): #percorre todas celulas da matriz
        for j in range(len(timeTableWithMaxPenalty[i])):
            neighborSolution = initialSolutionArg.copy()
            classNeighborSolution = copy.deepcopy(timeTableWithMaxPenalty)
            classNeighborSolution[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]] = classNeighborSolution[i][j]
            classNeighborSolution[i][j] = maxBlockValue
            neighborSolution[maxClassData] = copy.deepcopy(classNeighborSolution) 

            neighborSolutions.append(neighborSolution)

        print(neighborSolution)

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
        