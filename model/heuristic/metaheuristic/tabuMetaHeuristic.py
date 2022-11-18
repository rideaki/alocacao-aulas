import copy
import random
import numpy

from collections import deque
from model.business.solutionAnalyzer import globalSolutionPenalty, globalSolution
from model.business.comparator import areDifferentBlocks
from model.business.solutionAnalyzer import analyzeSolution
from model.constraints.teacherConstrainsts import SPARSE_DAYS_PENALTY, calculatePenalties
from model.exporter.csvGenericExporter import exportToGenericCsvFile
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT

META_HEURISTIC_CYCLES = 90
FINAL_OPTIMIZATION_CYCLES = 5
TABU_SIZE = 40

tabu = deque(maxlen=TABU_SIZE)

def searchTabuHeuristicSolution(solution, penaltiesTablesDict):
    tabu.clear()
    for i in range(META_HEURISTIC_CYCLES):
        exportToGenericCsvFile(solution, "log.csv")
        print("\n %d° Ciclo: " % i)
        solution = __searchBestNeighborSolution(solution.copy(), penaltiesTablesDict.copy())
        penaltiesTablesDict, penaltyValue = analyzeSolution(solution)
        if penaltyValue < SPARSE_DAYS_PENALTY:
            for j in range(FINAL_OPTIMIZATION_CYCLES):
                __optimizeLocalSolution(solution.copy(), penaltiesTablesDict, penaltyValue)
            return

def __optimizeLocalSolution(solutionArg, penaltiesTablesDict, penaltyValueArg):
    tabu.clear()
    officialSolution = solutionArg.copy()
    officialPenaltyValue = penaltyValueArg
    # Para cada turma
    for classData, penaltyTable in penaltiesTablesDict.copy().items(): #TODO iterar dict randomicamente
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

def __searchSolutionPermutingOneIndex(initialSolution, classData, index):
    neighborSolutions = __generateNeighborSolutions(initialSolution, classData, index)

    bestSolution = None
    bestSolutionPenalty = float('inf')
    for solution in neighborSolutions:
        _, solutionPenalty = calculatePenalties(solution)
        if (solutionPenalty <= bestSolutionPenalty):    
            bestSolution = solution
            bestSolutionPenalty = solutionPenalty
    
    print(str(classData.periodNumber) + classData.shift)
    print(str(index) + "<-" + str(bestSolution[classData][index[0]][index[1]]))
    return bestSolution


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
        