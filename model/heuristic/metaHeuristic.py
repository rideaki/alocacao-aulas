import copy
import dataLoader
import numpy

def searchMetaHeuristicSolution(initialSolutionArg, penaltiesTablesDict):
    maxClassData = None
    maxPenaltyIndexes = None
    maxClassData, maxPenaltyIndexes = __searchMaxPenalty(penaltiesTablesDict)
    print(str(maxClassData.periodNumber) + maxClassData.shift)
    print(maxPenaltyIndexes)
    neighborSolutions = __generateNeighborSolutions(initialSolutionArg, maxClassData, maxPenaltyIndexes)



#Gerando permutações da timeTable[maxClassData] com indices maxPenaltyIndexes
def __generateNeighborSolutions(initialSolution, maxClassData, maxPenaltyIndexes):
    neighborSolutions = []
    timeTableWithMaxPenalty = copy.deepcopy(initialSolution[maxClassData])
    maxBlockValue = timeTableWithMaxPenalty[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]]
    for i in range(len(timeTableWithMaxPenalty)): 
        for j in range(len(timeTableWithMaxPenalty[i])):
            neighborSolution = initialSolution.copy()
            classNeighborSolution = copy.deepcopy(timeTableWithMaxPenalty)
            classNeighborSolution[maxPenaltyIndexes[0]][maxPenaltyIndexes[1]] = classNeighborSolution[i][j]
            classNeighborSolution[i][j] = maxBlockValue
            __filterEqualSolution(maxClassData, neighborSolutions, timeTableWithMaxPenalty, neighborSolution, classNeighborSolution)
    return neighborSolutions

def __filterEqualSolution(maxClassData, neighborSolutions, timeTableWithMaxPenalty, neighborSolution, classNeighborSolution):
    if not __areEquivalentTables(classNeighborSolution, timeTableWithMaxPenalty):
        neighborSolution[maxClassData] = copy.deepcopy(classNeighborSolution) 
        neighborSolutions.append(neighborSolution)

#Verifica se duas timeTables são iguais ou equivalentes, ou seja, cuja alocação de blocos são as mesmas
def __areEquivalentTables(timeTable1, timeTable2):
    if numpy.array_equal(timeTable1, timeTable2):  #se as duas tabelas são iguais
        return True
    for i in range(len(timeTable1)):
        for j in range(len(timeTable1[i])):
            if __areDifferentBlocks(timeTable1[i][j], timeTable2[i][j]):
                return False
    return True

#Recebe indices de dois blocos, e retorna: 
# False: se os indices são iguais, ou se são blocos do mesmo componente curricular e mesmo professor
# True: caso contrário
def __areDifferentBlocks(block1Index, block2Index):
    if block1Index == block2Index:
        return False
    if (block1Index == None and block2Index != None) or (block1Index != None and block2Index == None):
        return True
    blocks = dataLoader.getBlocksCopy()
    block1 = blocks[block1Index]
    block2 = blocks[block2Index]
    return (block1.curricularComponentName != block2.curricularComponentName) or (
        block1.teacher.name != block2.teacher.name
    )               

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
        