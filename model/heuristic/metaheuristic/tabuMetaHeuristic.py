import copy
import numpy

from collections import deque
from model.business.comparator import areDifferentBlocks
from model.constraints.teacherConstrainsts import calculatePenalties

TABU_SIZE = 40

tabu = deque(maxlen=TABU_SIZE)

def searchTabuHeuristicSolution(initialSolution, penaltiesTablesDict):
    tabu.append(initialSolution)
    maxClassData = None
    maxPenaltyIndexes = None
    maxClassData, maxPenaltyIndexes = __searchMaxPenalty(penaltiesTablesDict)
    neighborSolutions = __generateNeighborSolutions(initialSolution, maxClassData, maxPenaltyIndexes)

    bestSolution = None
    bestSolutionPenalty = float('inf')
    for solution in neighborSolutions:
        penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
        if (solutionPenalty <= bestSolutionPenalty) and (solution not in tabu):    
            bestSolution = solution
            bestSolutionPenalty = solutionPenalty
    
    print(str(maxClassData.periodNumber) + maxClassData.shift)
    print(str(maxPenaltyIndexes) + "<-" + str(bestSolution[maxClassData][maxPenaltyIndexes[0]][maxPenaltyIndexes[1]]))
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
            __includeSolution(maxClassData, maxPenaltyIndexes, neighborSolutions, maxBlockValue, i, j, neighborSolution, classNeighborSolution)
    return neighborSolutions

#Inclui nova solução vizinha, se blocos permutados são diferentes
def __includeSolution(maxClassData, maxPenaltyIndexes, neighborSolutions, maxBlockValue, i, j, neighborSolution, classNeighborSolution):
    if areDifferentBlocks(maxBlockValue, classNeighborSolution[i][j]):
        classNeighborSolution[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]] = classNeighborSolution[i][j]
        classNeighborSolution[i][j] = maxBlockValue
        neighborSolution[maxClassData] = copy.deepcopy(classNeighborSolution) 
        neighborSolutions.append(neighborSolution)

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
        