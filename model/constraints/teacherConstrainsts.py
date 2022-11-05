from http.client import CONFLICT
from math import ceil
import numpy
import dataLoader
from model.business.tableFactory import constructClassTable
from model.constraints.entity.allocatedTeacher import AllocatedTeacher
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT

CONFLICT_PENALTY = 1000000
AVAILABILITY_PENALTY = 300
THREE_CONSECUTIVE_BLOCKS_PENALTY = 200
SPARSE_DAYS_PENALTY = 2

def calculatePenalties(timeTablesDict): #recebe dicionario[classData] = tabela horária de cada turma (classData)
    penaltiesTablesDict = {} #retorna dicionario[classData] = tabela de penalidades de cada turma (classData)

    allocatedTeachers = __returnEmptyAllocatedTeachersDict()
    blocks = dataLoader.getBlocksCopy()

    #para cada timeTable de cada turma
    for classData, timeTable in timeTablesDict.items():
        penaltiesTablesDict[classData] = constructClassTable(0)
        penaltyTable = penaltiesTablesDict[classData]

        __checkConsecutivesThreeBlocks(blocks, timeTable, penaltyTable)

        #para cada bloco de cada do timeTable da turma
        for indexesPair, blockAllocation in numpy.ndenumerate(timeTable):
            if(blockAllocation == None):
                continue #pula a iteração atual
            block = blocks[blockAllocation]
            teacher = block.teacher
            teacherName = teacher.name
            allocatedTeacher = allocatedTeachers[teacherName]
            allocationTable = allocatedTeacher.allocationsTables[block.classData.shift]
            
            __checkConflict(penaltyTable, indexesPair, block, allocationTable)
            __checkUnavailableDay(penaltyTable, indexesPair, teacher)
    
    #para cada professor alocado
    __checkSparseDays(penaltiesTablesDict, allocatedTeachers) 

    penaltiesTotalValue = __calculatePenaltiesTotalValues(penaltiesTablesDict)
    print(penaltiesTotalValue)

    return penaltiesTablesDict, penaltiesTotalValue

#VERIFICA SE A DISTRIBUIÇÃO DE ALOCAÇÕES SE ESPALHOU POR MUITOS DIAS PARA O PROFESSOR
def __checkSparseDays(penaltiesTablesDict, allocatedTeachers):
    #para cada professor alocado
    for teacherName, allocatedTeacher in allocatedTeachers.items():
        concatenatedAllocationTable = __concatenateShiftsAllocationTables(allocatedTeacher)
        if(concatenatedAllocationTable is None):
            continue #professor não foi alocado, portanto não há penalidade. Pula para o próx. professor
        numberOfBlocksAllocated = numpy.where(concatenatedAllocationTable != None, 1, 0).sum() 
        daysOfWeekAllocatedBoolean = ~numpy.all(concatenatedAllocationTable == None, axis = 0)
        numberOfDaysAllocated = daysOfWeekAllocatedBoolean.sum()
        numberOfRowsInConcatenatedTable = 6 #len(concatenatedAllocationTable) #[:,0].size
        minDaysToBeAllocated = ceil(numberOfBlocksAllocated/numberOfRowsInConcatenatedTable)
        if (numberOfDaysAllocated <= minDaysToBeAllocated) or (
            numberOfDaysAllocated == 2 and numberOfBlocksAllocated == numberOfRowsInConcatenatedTable):  #contem disciplinas com 3 blocos
            continue #número de dias alocado já é mínimo, portanto não há penalidade. Pula para o próx. professor
        daysOfWeekAllocated = numpy.where(daysOfWeekAllocatedBoolean == True)[0]
        
        __applyPenaltiesOnFirstDay(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated)
        __applyPenaltiesOnLastDaty(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated)

#Aplica penalidades no primeiro dia esparco alocado
def __applyPenaltiesOnFirstDay(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated):
    firstDayAllocated = daysOfWeekAllocated[0]
    numberOfBlocksInFirstDay = numpy.where(concatenatedAllocationTable[:,firstDayAllocated] != None, 1, 0).sum()
    penaltyByBlockInFirstDay = (numberOfDaysAllocated - minDaysToBeAllocated)*SPARSE_DAYS_PENALTY/numberOfBlocksInFirstDay
    for index, block in enumerate(list(zip(*concatenatedAllocationTable))[firstDayAllocated]): # zip(*matrix) = transposed of matrix
        if block == None:
            continue
        penaltiesTablesDict[block.classData][index % NUMBER_OF_BLOCKS_IN_SHIFT][firstDayAllocated] += penaltyByBlockInFirstDay

#Aplica penalidades no ultimo dia esparco alocado
def __applyPenaltiesOnLastDaty(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated):
    lastDayAllocated = daysOfWeekAllocated[-1] #em python, indice -1 retorna o ultimo elemento
    numberOfBlocksInLastDay = numpy.where(concatenatedAllocationTable[:,lastDayAllocated] != None, 1, 0).sum()
    penaltyByBlockInLastDay = (numberOfDaysAllocated - minDaysToBeAllocated)*SPARSE_DAYS_PENALTY/numberOfBlocksInLastDay
    for index, block in enumerate(list(zip(*concatenatedAllocationTable))[lastDayAllocated]): # zip(*matrix) = transposed of matrix
        if block == None:
            continue
        penaltiesTablesDict[block.classData][index % NUMBER_OF_BLOCKS_IN_SHIFT][lastDayAllocated] += penaltyByBlockInLastDay

#Concatena as tabelas de alocação do verticalmente
def __concatenateShiftsAllocationTables(allocatedTeacher):
    returnConcatenedTable = None
    #Para cada turno
    for shift, allocationTableByShift in allocatedTeacher.allocationsTables.items():
        if (numpy.array(allocationTableByShift) == None).all():  #Se não há alocação no turno, não concatena a tabela
            continue
        if returnConcatenedTable is None:
            returnConcatenedTable = allocationTableByShift
        else:
            returnConcatenedTable = numpy.concatenate((returnConcatenedTable, allocationTableByShift), axis=0) #axis=0 -> conc. vertical
    return numpy.array(returnConcatenedTable)

#VERIFICACAO DE DISCIPLINA COM 3 BLOCOS SEGUIDOS NO MESMO TURNO
def __checkConsecutivesThreeBlocks(blocks, timeTable, penaltyTable):
    for dayOfWeek in range(5):
        if((timeTable[0][dayOfWeek] != None) and (timeTable[1][dayOfWeek] != None) and (timeTable[2][dayOfWeek] != None)):
            firstBlockIndex =  timeTable[0][dayOfWeek]
            firstCurricularComponentName = blocks[firstBlockIndex].curricularComponentName
            secondBlockIndex = timeTable[1][dayOfWeek]
            secondCurricularComponentName = blocks[secondBlockIndex].curricularComponentName
            thirdBlockIndex = timeTable[2][dayOfWeek]
            thirdCurricularComponentName = blocks[thirdBlockIndex].curricularComponentName
            if(firstCurricularComponentName == secondCurricularComponentName == thirdCurricularComponentName):
                #disciplina de 3 blocos está no mesmo dia
                penaltyTable[0][dayOfWeek] += THREE_CONSECUTIVE_BLOCKS_PENALTY/2 #marca penalidade na primeira aula do turno
                penaltyTable[2][dayOfWeek] += THREE_CONSECUTIVE_BLOCKS_PENALTY/2 #marca penalidade na u aula do turno

# VERIFICACAO DE CONFLITO e ATUALIZA TABELA DE ALOCACAO DO PROFESSOR
def __checkConflict(penaltyTable, indexesPair, block, allocationTable):
    if (allocationTable[indexesPair[0]][indexesPair[1]] != None):  #conflito: horário já alocado para o professor!
        penaltyTable[indexesPair[0]][indexesPair[1]] += CONFLICT_PENALTY
    else: #aloca bloco na allocationTable do professor
        allocationTable[indexesPair[0]][indexesPair[1]] = block

# VERIFICACAO DE ALOCACAO FORA DA DISPONIBILIDADE DO PROFESSOR
def __checkUnavailableDay(penaltyTable, indexesPair, teacher):
    dayOfWeekAllocated = indexesPair[1]
    if (dayOfWeekAllocated not in teacher.getAvailabilitiesCopy()):
        penaltyTable[indexesPair[0]][indexesPair[1]] += AVAILABILITY_PENALTY

def __returnEmptyAllocatedTeachersDict():
    empytAllocatedTeachers = {}
    teachers =  dataLoader.getTeachersCopy()
    for teacherName, teacher in teachers.items():
        empytAllocatedTeachers[teacher.name] = AllocatedTeacher(teacherName, teacher.getAvailabilitiesCopy())
    return empytAllocatedTeachers

def __calculatePenaltiesTotalValues(penaltiesTablesDict):
    penaltiesTotalValue = 0
    for timeTable in penaltiesTablesDict.values():
        penaltiesTotalValue += numpy.sum(timeTable)
    return penaltiesTotalValue
