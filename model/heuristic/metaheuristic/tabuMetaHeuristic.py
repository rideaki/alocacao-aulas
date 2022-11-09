import copy
import random
import numpy

from collections import deque
from model.business.solutionAnalyzer import globalSolutionPenalty, globalSolution
from model.business.comparator import areDifferentBlocks
from model.business.solutionAnalyzer import analyzeSolution
from model.constraints.teacherConstrainsts import SPARSE_DAYS_PENALTY, calculatePenalties

META_HEURISTIC_CYCLES = 90
TABU_SIZE = 40

tabu = deque(maxlen=TABU_SIZE)

def searchTabuHeuristicSolution(solution, globalPenaltiesTables):
    __searchSolutionsInCycles(solution, globalPenaltiesTables)
    if globalSolutionPenalty < SPARSE_DAYS_PENALTY:
        globalPenaltiesTables = calculatePenalties(globalSolution)    
        __searchSolutionsInCycles(globalSolution, globalPenaltiesTables)

def __searchSolutionsInCycles(solution, penaltiesTablesDict):
    tabu.clear()
    for i in range(META_HEURISTIC_CYCLES):
        print("\n %d° Ciclo: " % i)
        solution = __searchBestNeighborSolution(solution.copy(), penaltiesTablesDict.copy())
        penaltiesTablesDict = analyzeSolution(solution)

def __searchBestNeighborSolution(initialSolution, penaltiesTablesDict):
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
        maxLocalValue = numpy.amax(penaltyTable)
        if maxLocalValue < maxGlobalPenalty:
            continue #maior penalidade da tabela não é o maximo de todas -> pula iteracao
        maxGlobalPenalty = maxLocalValue
        maxClassData = classData
        maxPenaltyIndexes = list(zip(*numpy.where(penaltyTable == maxLocalValue)))
        maxPenaltyIndex = random.choice(maxPenaltyIndexes)

    return maxClassData, maxPenaltyIndex
        