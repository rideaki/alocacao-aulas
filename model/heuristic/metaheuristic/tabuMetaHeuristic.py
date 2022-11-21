import copy
import random
import numpy

from collections import deque
from model.business.comparator import areDifferentBlocks
from model.business.solutionAnalyzer import analyzeSolution
from model.constraints.teacherConstrainsts import *

META_HEURISTIC_CYCLES = 20
TABU_SIZE = 10

tabu = deque(maxlen=TABU_SIZE)

def searchTabuHeuristicSolution(solution):
    penaltiesTablesDict, _ = calculatePenalties(solution)
    for i in range(META_HEURISTIC_CYCLES):
        tabu.clear()
        #exportToGenericCsvFile(solution, "log.csv")
        print("\n %d° Ciclo: " % i)
        solution = __searchBestNeighborSolution(solution.copy(), penaltiesTablesDict.copy())
        penaltiesTablesDict, penaltyValue = analyzeSolution(solution)

        #Refinamento final para otimização local: eliminação de janelas (horários vagos) do professor
        if penaltyValue < CONSECUTIVE_BLOCKS_PENALTY:
            isImproved = True
            while isImproved:
                solution, isImproved = __optimizeLocalSolution(solution.copy(), penaltiesTablesDict, penaltyValue)
                penaltiesTablesDict, penaltyValue = analyzeSolution(solution)
            return

def __optimizeLocalSolution(solutionArg, penaltiesTablesDict, penaltyValueArg):
    tabu.clear()
    isImproved = False
    officialSolution = solutionArg.copy()
    officialPenaltyValue = penaltyValueArg
    # Para cada turma
    for classData, penaltyTable in penaltiesTablesDict.copy().items():
        #Para cada penalidade escolhida randomicamente
        rowsNumber = len(penaltyTable)
        columnsNumber = len(penaltyTable[0])
        coords = [(x,y) for x in range(rowsNumber) for y in range(columnsNumber)]
        random.shuffle(coords)
        for i,j in coords:
            cellPenalty = penaltyTable[i][j]
            if(cellPenalty == 0):
                continue    
            penaltyIndex = [i,j]
            print("\n Melhoria local: ", penaltyIndex)
            print(str(classData))
            bestNeighborSolution = __searchSolutionPermutingOneIndex(officialSolution.copy(), classData, penaltyIndex)
            _, neighborPenalty = analyzeSolution(bestNeighborSolution)
            if neighborPenalty < officialPenaltyValue:
                officialSolution = bestNeighborSolution
                officialPenaltyValue = neighborPenalty
                isImproved = True

    return officialSolution, isImproved

def __searchSolutionPermutingOneIndex(initialSolution, classData, index):
    neighborSolutions = __generateFinalNeighborSolutions(initialSolution, classData, index)

    bestSolution = None
    bestSolutionPenalty = float('inf')
    for solution in neighborSolutions:
        _, solutionPenalty = calculatePenalties(solution)
        if (solutionPenalty < bestSolutionPenalty):    
            bestSolution = solution
            bestSolutionPenalty = solutionPenalty
    
    return bestSolution


def __searchBestNeighborSolution(initialSolution, penaltiesTablesDict):
    tabu.append(initialSolution)
    maxClassData = None
    maxPenaltyIndexes = None
    maxClassData, maxPenaltyIndexes = __searchMaxPenalty(penaltiesTablesDict)
    neighborSolutions = __generateNeighborSolutions(initialSolution, maxClassData, maxPenaltyIndexes)

    bestSolution = None
    bestSolutionPenalty = float('inf')
    random.shuffle(neighborSolutions)
    for solution in neighborSolutions:
        #exportToGenericCsvFile(solution, "log.csv")
        penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
        if (solutionPenalty < bestSolutionPenalty) and (
        solution not in tabu
        ):    
            bestSolution = solution
            bestSolutionPenalty = solutionPenalty
    
    print(str(maxClassData.periodNumber) + maxClassData.shift)
    print(str(maxPenaltyIndexes) + "<-" + str(bestSolution[maxClassData][maxPenaltyIndexes[0]][maxPenaltyIndexes[1]]))
    return bestSolution

#Gerando permutações da timeTable[classData] com indices indexToPermute, refinamento final
def __generateFinalNeighborSolutions(initialSolution, classData, indexToPermute):
    neighborSolutions = []
    timeTable = copy.deepcopy(initialSolution[classData])
    blockIndex = timeTable[indexToPermute[0]][indexToPermute[1]]
    block = dataLoader.getBlocks()[blockIndex]
    for i in range(len(timeTable)): 
        teacherAvailabilities = block.teacher.getAvailabilitiesCopy()
        for j in teacherAvailabilities:
            neighborSolution = initialSolution.copy()
            classNeighborSolution = copy.deepcopy(timeTable)
            __includeSolution(classData, indexToPermute, neighborSolutions, blockIndex, i, j, neighborSolution, classNeighborSolution)
    return neighborSolutions


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
    maxGlobalPenalty = -1
    # Para cada turma
    for classData, penaltyTable in penaltiesTablesDict.copy().items():
        maxLocalValue = numpy.amax(penaltyTable)
        if maxLocalValue <= maxGlobalPenalty:
            continue #maior penalidade da tabela não é o maximo de todas -> pula iteracao
        maxGlobalPenalty = maxLocalValue
        maxClassData = classData
        maxPenaltyIndexes = list(zip(*numpy.where(penaltyTable == maxLocalValue)))
        maxPenaltyIndex = random.choice(maxPenaltyIndexes)

    return maxClassData, maxPenaltyIndex
        