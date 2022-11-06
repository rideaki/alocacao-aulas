import copy
import numpy

from model.business.comparator import areDifferentBlocks
from model.constraints.teacherConstrainsts import calculatePenalties

def searchMetaHeuristicSolution(initialSolutionArg, penaltiesTablesDict):
    maxClassData = None
    maxPenaltyIndexes = None
    maxClassData, maxPenaltyIndexes = __searchMaxPenalty(penaltiesTablesDict)
    print(str(maxClassData.periodNumber) + maxClassData.shift)
    print(maxPenaltyIndexes)
    neighborSolutions = __generateNeighborSolutions(initialSolutionArg, maxClassData, maxPenaltyIndexes)

    bestSolution = None
    bestSolutionPenalty = float('inf')
    for solution in neighborSolutions:
        penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
        if(solutionPenalty <= bestSolutionPenalty):    
            bestSolution = solution
            bestSolutionPenalty = solutionPenalty
    return bestSolution

#Gerando permutações da timeTable[maxClassData] com indices maxPenaltyIndexes
def __generateNeighborSolutions(initialSolution, maxClassData, maxPenaltyIndexes):
    neighborSolutions = []
    timeTableWithMaxPenalty = copy.deepcopy(initialSolution[maxClassData])
    maxBlockValue = timeTableWithMaxPenalty[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]]
    for i in range(len(timeTableWithMaxPenalty)): 
        for j in range(len(timeTableWithMaxPenalty[i])):
            neighborSolution = initialSolution.copy()
            classNeighborSolution = copy.deepcopy(timeTableWithMaxPenalty)
            if areDifferentBlocks(maxBlockValue, classNeighborSolution[i][j]):
                classNeighborSolution[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]] = classNeighborSolution[i][j]
                classNeighborSolution[i][j] = maxBlockValue
                neighborSolution[maxClassData] = copy.deepcopy(classNeighborSolution) 
                neighborSolutions.append(neighborSolution)
    return neighborSolutions

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
        